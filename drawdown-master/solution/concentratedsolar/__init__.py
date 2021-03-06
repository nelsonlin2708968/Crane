"""Concentrated Solar Power (CSP) solution model.
   Excel filename: CSP_RRS_ELECGEN_v1.1b_24Oct18.xlsm
"""

import pathlib

import pandas as pd

from model import adoptiondata
from model import advanced_controls
from model import ch4calcs
from model import co2calcs
from model import emissionsfactors
from model import firstcost
from model import helpertables
from model import operatingcost
from model import unitadoption

from solution import rrs

from model import tam
scenarios = {
  'PDS-4p2050-Drawdown Plausible (Revison Case)': advanced_controls.AdvancedControls(
      report_start_year = 2020, report_end_year = 2050, 

      pds_2014_cost = 6658.140808432578, ref_2014_cost = 6658.140808432578, 
      conv_2014_cost = 2010.0317085196398, 
      soln_first_cost_efficiency_rate = 0.146, 
      conv_first_cost_efficiency_rate = 0.02, soln_first_cost_below_conv = True, 
      npv_discount_rate = 0.094, 

      co2eq_conversion_source = 'AR5 with feedback', 
      soln_indirect_co2_per_iunit = 38928.57142857143, 
      conv_indirect_co2_per_unit = 0.0, conv_indirect_co2_is_iunits = False, 

      soln_lifetime_capacity = 83815.59999999999, soln_avg_annual_use = 3047.8399999999992, 
      conv_lifetime_capacity = 178770.5, conv_avg_annual_use = 4967.648441815689, 

      soln_var_oper_cost_per_funit = 0.02451965, soln_fuel_cost_per_funit = 0.0, 
      soln_fixed_oper_cost_per_iunit = 66.0956544050825, 
      conv_var_oper_cost_per_funit = 0.0047524321679508165, conv_fuel_cost_per_funit = 0.09, 
      conv_fixed_oper_cost_per_iunit = 32.89064573433522, 

      emissions_grid_source = 'Meta-Analysis', emissions_grid_range = 'Mean', 
      emissions_use_co2eq = True, 

      soln_ref_adoption_regional_data = False, soln_pds_adoption_regional_data = False, 
      soln_pds_adoption_basis = 'Existing Adoption Prognostications', 
      soln_pds_adoption_prognostication_source = 'Ambitious Cases', 
      soln_pds_adoption_prognostication_trend = '3rd Poly', 
      soln_pds_adoption_prognostication_growth = 'Low', 
      source_until_2014 = 'ALL SOURCES', 
      ref_source_post_2014 = 'Baseline Cases', 
      pds_source_post_2014 = 'Drawdown TAM: Drawdown TAM - Post Integration - Plausible Scenario', 

      solution_category = 'REPLACEMENT', 
    ),
  'PDS-8p2050-Drawdown Scenario (Revision Case)': advanced_controls.AdvancedControls(
      report_start_year = 2020, report_end_year = 2050, 

      pds_2014_cost = 6658.140808432578, ref_2014_cost = 6658.140808432578, 
      conv_2014_cost = 2010.0317085196398, 
      soln_first_cost_efficiency_rate = 0.146, 
      conv_first_cost_efficiency_rate = 0.02, soln_first_cost_below_conv = True, 
      npv_discount_rate = 0.094, 

      co2eq_conversion_source = 'AR5 with feedback', 
      soln_indirect_co2_per_iunit = 38928.57142857143, 
      conv_indirect_co2_per_unit = 0.0, conv_indirect_co2_is_iunits = False, 

      soln_lifetime_capacity = 83815.59999999999, soln_avg_annual_use = 3047.8399999999992, 
      conv_lifetime_capacity = 178770.5, conv_avg_annual_use = 4967.648441815689, 

      soln_var_oper_cost_per_funit = 0.02451965, soln_fuel_cost_per_funit = 0.0, 
      soln_fixed_oper_cost_per_iunit = 66.0956544050825, 
      conv_var_oper_cost_per_funit = 0.0047524321679508165, conv_fuel_cost_per_funit = 0.09, 
      conv_fixed_oper_cost_per_iunit = 32.89064573433522, 

      emissions_grid_source = 'Meta-Analysis', emissions_grid_range = 'Mean', 
      emissions_use_co2eq = True, 

      soln_ref_adoption_regional_data = False, soln_pds_adoption_regional_data = False, 
      soln_pds_adoption_basis = 'Existing Adoption Prognostications', 
      soln_pds_adoption_prognostication_source = 'Ambitious Cases', 
      soln_pds_adoption_prognostication_trend = '3rd Poly', 
      soln_pds_adoption_prognostication_growth = 'Medium', 
      source_until_2014 = 'ALL SOURCES', 
      ref_source_post_2014 = 'Baseline Cases', 
      pds_source_post_2014 = 'Drawdown TAM: Drawdown TAM - Post Integration - Drawdown Scenario', 

      solution_category = 'REPLACEMENT', 
    ),
  'PDS-8p2050-Drawdown Optimum Scenario (Revision Case)': advanced_controls.AdvancedControls(
      report_start_year = 2020, report_end_year = 2050, 

      pds_2014_cost = 6658.140808432578, ref_2014_cost = 6658.140808432578, 
      conv_2014_cost = 2010.0317085196398, 
      soln_first_cost_efficiency_rate = 0.146, 
      conv_first_cost_efficiency_rate = 0.02, soln_first_cost_below_conv = True, 
      npv_discount_rate = 0.094, 

      co2eq_conversion_source = 'AR5 with feedback', 
      soln_indirect_co2_per_iunit = 38928.57142857143, 
      conv_indirect_co2_per_unit = 0.0, conv_indirect_co2_is_iunits = False, 

      soln_lifetime_capacity = 83815.59999999999, soln_avg_annual_use = 3047.8399999999992, 
      conv_lifetime_capacity = 178770.5, conv_avg_annual_use = 4967.648441815689, 

      soln_var_oper_cost_per_funit = 0.02451965, soln_fuel_cost_per_funit = 0.0, 
      soln_fixed_oper_cost_per_iunit = 66.0956544050825, 
      conv_var_oper_cost_per_funit = 0.0047524321679508165, conv_fuel_cost_per_funit = 0.09, 
      conv_fixed_oper_cost_per_iunit = 32.89064573433522, 

      emissions_grid_source = 'Meta-Analysis', emissions_grid_range = 'Mean', 
      emissions_use_co2eq = True, 

      soln_ref_adoption_regional_data = False, soln_pds_adoption_regional_data = False, 
      soln_pds_adoption_basis = 'Existing Adoption Prognostications', 
      soln_pds_adoption_prognostication_source = 'Ambitious Cases', 
      soln_pds_adoption_prognostication_trend = '3rd Poly', 
      soln_pds_adoption_prognostication_growth = 'Medium', 
      source_until_2014 = 'ALL SOURCES', 
      ref_source_post_2014 = 'Baseline Cases', 
      pds_source_post_2014 = 'Drawdown TAM: Drawdown TAM - Post Integration - Optimum Scenario', 

      solution_category = 'REPLACEMENT', 
    ),
  'PDS-4p2050-Plausible (Book Ed.1)': advanced_controls.AdvancedControls(
      report_start_year = 2020, report_end_year = 2050, 

      pds_2014_cost = 6603.183768010948, ref_2014_cost = 6603.183768010948, 
      conv_2014_cost = 2010.0317085196398, 
      soln_first_cost_efficiency_rate = 0.146, 
      conv_first_cost_efficiency_rate = 0.02, soln_first_cost_below_conv = True, 
      npv_discount_rate = 0.094, 

      co2eq_conversion_source = 'AR5 with feedback', 
      soln_indirect_co2_per_iunit = 33916.666666666664, 
      conv_indirect_co2_per_unit = 0.0, conv_indirect_co2_is_iunits = False, 

      soln_lifetime_capacity = 83815.59999999999, soln_avg_annual_use = 3047.8399999999992, 
      conv_lifetime_capacity = 182411.2757676607, conv_avg_annual_use = 4946.8401873420025, 

      soln_var_oper_cost_per_funit = 0.03269286666666667, soln_fuel_cost_per_funit = 0.0, 
      soln_fixed_oper_cost_per_iunit = 96.221308810165, 
      conv_var_oper_cost_per_funit = 0.003752690403548987, conv_fuel_cost_per_funit = 0.07, 
      conv_fixed_oper_cost_per_iunit = 32.951404311078015, 

      emissions_grid_source = 'Meta-Analysis', emissions_grid_range = 'Mean', 
      emissions_use_co2eq = True, 

      soln_ref_adoption_regional_data = False, soln_pds_adoption_regional_data = False, 
      soln_pds_adoption_basis = 'Existing Adoption Prognostications', 
      soln_pds_adoption_prognostication_source = 'Ambitious Cases', 
      soln_pds_adoption_prognostication_trend = '3rd Poly', 
      soln_pds_adoption_prognostication_growth = 'Low', 
      source_until_2014 = 'ALL SOURCES', 
      ref_source_post_2014 = 'Baseline Cases', 
      pds_source_post_2014 = 'Drawdown TAM: Drawdown TAM - Post Integration - Plausible Scenario', 

      solution_category = 'REPLACEMENT', 
    ),
  'PDS-8p2050-Drawdown (Book Ed. 1)': advanced_controls.AdvancedControls(
      report_start_year = 2020, report_end_year = 2050, 

      pds_2014_cost = 6603.183768010948, ref_2014_cost = 6603.183768010948, 
      conv_2014_cost = 2010.0317085196398, 
      soln_first_cost_efficiency_rate = 0.146, 
      conv_first_cost_efficiency_rate = 0.02, soln_first_cost_below_conv = True, 
      npv_discount_rate = 0.094, 

      co2eq_conversion_source = 'AR5 with feedback', 
      soln_indirect_co2_per_iunit = 33916.666666666664, 
      conv_indirect_co2_per_unit = 0.0, conv_indirect_co2_is_iunits = False, 

      soln_lifetime_capacity = 83815.59999999999, soln_avg_annual_use = 3047.8399999999992, 
      conv_lifetime_capacity = 182411.2757676607, conv_avg_annual_use = 4946.8401873420025, 

      soln_var_oper_cost_per_funit = 0.03269286666666667, soln_fuel_cost_per_funit = 0.0, 
      soln_fixed_oper_cost_per_iunit = 96.221308810165, 
      conv_var_oper_cost_per_funit = 0.003752690403548987, conv_fuel_cost_per_funit = 0.07, 
      conv_fixed_oper_cost_per_iunit = 32.951404311078015, 

      emissions_grid_source = 'Meta-Analysis', emissions_grid_range = 'Mean', 
      emissions_use_co2eq = True, 

      soln_ref_adoption_regional_data = False, soln_pds_adoption_regional_data = False, 
      soln_pds_adoption_basis = 'Existing Adoption Prognostications', 
      soln_pds_adoption_prognostication_source = 'Ambitious Cases', 
      soln_pds_adoption_prognostication_trend = '3rd Poly', 
      soln_pds_adoption_prognostication_growth = 'Medium', 
      source_until_2014 = 'ALL SOURCES', 
      ref_source_post_2014 = 'Baseline Cases', 
      pds_source_post_2014 = 'Drawdown TAM: Drawdown TAM - Post Integration - Drawdown Scenario', 

      solution_category = 'REPLACEMENT', 
    ),
  'PDS-8p2050-Optimum (Book Ed. 1)': advanced_controls.AdvancedControls(
      report_start_year = 2020, report_end_year = 2050, 

      pds_2014_cost = 6603.183768010948, ref_2014_cost = 6603.183768010948, 
      conv_2014_cost = 2010.0317085196398, 
      soln_first_cost_efficiency_rate = 0.146, 
      conv_first_cost_efficiency_rate = 0.02, soln_first_cost_below_conv = True, 
      npv_discount_rate = 0.094, 

      co2eq_conversion_source = 'AR5 with feedback', 
      soln_indirect_co2_per_iunit = 33916.666666666664, 
      conv_indirect_co2_per_unit = 0.0, conv_indirect_co2_is_iunits = False, 

      soln_lifetime_capacity = 83815.59999999999, soln_avg_annual_use = 3047.8399999999992, 
      conv_lifetime_capacity = 182411.2757676607, conv_avg_annual_use = 4946.8401873420025, 

      soln_var_oper_cost_per_funit = 0.03269286666666667, soln_fuel_cost_per_funit = 0.0, 
      soln_fixed_oper_cost_per_iunit = 96.221308810165, 
      conv_var_oper_cost_per_funit = 0.003752690403548987, conv_fuel_cost_per_funit = 0.07, 
      conv_fixed_oper_cost_per_iunit = 32.951404311078015, 

      emissions_grid_source = 'Meta-Analysis', emissions_grid_range = 'Mean', 
      emissions_use_co2eq = True, 

      soln_ref_adoption_regional_data = False, soln_pds_adoption_regional_data = False, 
      soln_pds_adoption_basis = 'Existing Adoption Prognostications', 
      soln_pds_adoption_prognostication_source = 'Ambitious Cases', 
      soln_pds_adoption_prognostication_trend = '3rd Poly', 
      soln_pds_adoption_prognostication_growth = 'Medium', 
      source_until_2014 = 'ALL SOURCES', 
      ref_source_post_2014 = 'Baseline Cases', 
      pds_source_post_2014 = 'Drawdown TAM: Drawdown TAM - Post Integration - Optimum Scenario', 

      solution_category = 'REPLACEMENT', 
    ),
}

class ConcentratedSolar:
  name = 'Concentrated Solar Power (CSP)'
  units = {
    "implementation unit": "TW",
    "functional unit": "TWh",
    "first cost": "US$B",
    "operating cost": "US$B",
  }

  def __init__(self, scenario=None):
    datadir = str(pathlib.Path(__file__).parents[2].joinpath('data'))
    parentdir = pathlib.Path(__file__).parents[1]
    thisdir = pathlib.Path(__file__).parents[0]
    if scenario is None:
      scenario = 'PDS-4p2050-Drawdown Plausible (Revison Case)'
    self.scenario = scenario
    self.ac = scenarios[scenario]

    tamconfig_list = [
      ['param', 'World', 'PDS World', 'OECD90', 'Eastern Europe', 'Asia (Sans Japan)',
       'Middle East and Africa', 'Latin America', 'China', 'India', 'EU', 'USA'],
      ['source_until_2014', self.ac.source_until_2014, self.ac.source_until_2014,
       self.ac.source_until_2014, self.ac.source_until_2014, self.ac.source_until_2014,
       self.ac.source_until_2014, self.ac.source_until_2014, self.ac.source_until_2014,
       self.ac.source_until_2014, self.ac.source_until_2014, self.ac.source_until_2014],
      ['source_after_2014', self.ac.ref_source_post_2014, self.ac.pds_source_post_2014,
       'ALL SOURCES', 'ALL SOURCES', 'ALL SOURCES', 'ALL SOURCES', 'ALL SOURCES', 'ALL SOURCES',
       'ALL SOURCES', 'ALL SOURCES', 'ALL SOURCES'],
      ['trend', '3rd Poly', '3rd Poly',
       '3rd Poly', '3rd Poly', '3rd Poly', '3rd Poly', '3rd Poly', '3rd Poly',
       '3rd Poly', '3rd Poly', '3rd Poly'],
      ['growth', 'Medium', 'Medium', 'Medium', 'Medium',
       'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium'],
      ['low_sd_mult', 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
      ['high_sd_mult', 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]]
    tamconfig = pd.DataFrame(tamconfig_list[1:], columns=tamconfig_list[0]).set_index('param')
    self.tm = tam.TAM(tamconfig=tamconfig, tam_ref_data_sources=rrs.tam_ref_data_sources,
      tam_pds_data_sources=rrs.tam_pds_data_sources)
    ref_tam_per_region=self.tm.ref_tam_per_region()
    pds_tam_per_region=self.tm.pds_tam_per_region()

    adconfig_list = [
      ['param', 'World', 'OECD90', 'Eastern Europe', 'Asia (Sans Japan)',
       'Middle East and Africa', 'Latin America', 'China', 'India', 'EU', 'USA'],
      ['trend', self.ac.soln_pds_adoption_prognostication_trend, '3rd Poly',
       '3rd Poly', '3rd Poly', '3rd Poly', '3rd Poly', '3rd Poly',
       '3rd Poly', '3rd Poly', '3rd Poly'],
      ['growth', self.ac.soln_pds_adoption_prognostication_growth, 'Medium',
       'Medium', 'Medium', 'Medium', 'Medium', 'Medium',
       'Medium', 'Medium', 'Medium'],
      ['low_sd_mult', 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
      ['high_sd_mult', 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]]
    adconfig = pd.DataFrame(adconfig_list[1:], columns=adconfig_list[0]).set_index('param')
    ad_data_sources = {
      'Baseline Cases': {
        'Based on: IEA ETP 2016 - 6DS': str(thisdir.joinpath('ad_based_on_IEA_ETP_2016_6DS.csv')),
        'Based on: AMPERE MESSAGE REFpol': str(thisdir.joinpath('ad_based_on_AMPERE_2014_MESSAGE_MACRO_Reference.csv')),
        'Based on: AMPERE GEM E3 REFpol': str(thisdir.joinpath('ad_based_on_AMPERE_2014_GEM_E3_Reference.csv')),
        'Based on: AMPERE IMAGE REFpol': str(thisdir.joinpath('ad_based_on_AMPERE_2014_IMAGE_TIMER_Reference.csv')),
      },
      'Conservative Cases': {
        'Based on: IEA ETP 2016 - 4DS': str(thisdir.joinpath('ad_based_on_IEA_ETP_2016_4DS.csv')),
        'Based on: AMPERE MESSAGE 550': str(thisdir.joinpath('ad_based_on_AMPERE_2014_MESSAGE_MACRO_550.csv')),
        'Based on: AMPERE GEM E3 550': str(thisdir.joinpath('ad_based_on_AMPERE_2014_GEM_E3_550.csv')),
        'Based on: AMPERE IMAGE 550': str(thisdir.joinpath('ad_based_on_AMPERE_2014_IMAGE_TIMER_550.csv')),
        'Based on: Greenpeace Solar Thermal Elc Global Outlook 2016 (Moderate Scenario)': str(thisdir.joinpath('ad_based_on_Greenpeace_2016_Solar_Thermal_Moderate.csv')),
      },
      'Ambitious Cases': {
        'Based on: IEA ETP 2016 - 2DS': str(thisdir.joinpath('ad_based_on_IEA_ETP_2016_2DS.csv')),
        'Based on: AMPERE MESSAGE 450': str(thisdir.joinpath('ad_based_on_AMPERE_2014_MESSAGE_MACRO_450.csv')),
        'Based on: AMPERE GEM E3 450': str(thisdir.joinpath('ad_based_on_AMPERE_2014_GEM_E3_450.csv')),
        'Based on: AMPERE IMAGE 450': str(thisdir.joinpath('ad_based_on_AMPERE_2014_IMAGE_TIMER_450.csv')),
        'Based on: Greenpeace 2015 Energy Revolution Scenario': str(thisdir.joinpath('ad_based_on_Greenpeace_2015_Energy_Revolution.csv')),
        'Based on: Greenpeace Solar Thermal Elc Global Outlook 2016 (Advanced Scenario)': str(thisdir.joinpath('ad_based_on_Greenpeace_2016_Solar_Thermal_Advanced.csv')),
      },
      '100% Case': {
        'Based on: Greenpeace 2015 Advanced Energy Revolution Scenario': str(thisdir.joinpath('ad_based_on_Greenpeace_2015_Advanced_Revolution.csv')),
      },
    }
    self.ad = adoptiondata.AdoptionData(ac=self.ac, data_sources=ad_data_sources, adconfig=adconfig)

    ht_ref_datapoints = pd.DataFrame([
      [2014, 9.004, 8.159, 0.0, 0.334,
       0.511, 0.0, 0.007, 0.321,
       5.467, 2.688],
      [2050, 21.777061894912606, 10.59542672925403, 0.0, 0.9541428488661906,
       0.0, 0.0, 0.01475775297552966, 1.6741535160849408,
       7.203375011275469, 3.361931634481479]],
      columns=['Year', 'World', 'OECD90', 'Eastern Europe', 'Asia (Sans Japan)',
          'Middle East and Africa', 'Latin America', 'China', 'India', 'EU', 'USA']).set_index('Year')
    ht_pds_datapoints = pd.DataFrame([
      [2014, 9.004, 8.159, 0.0, 0.334,
       0.511, 0.0, 0.007, 0.321,
       5.467, 2.688],
      [2050, 0.0, 0.0, 0.0, 0.0,
       0.0, 0.0, 0.0, 0.0,
       0.0, 0.0]],
      columns=['Year', 'World', 'OECD90', 'Eastern Europe', 'Asia (Sans Japan)',
          'Middle East and Africa', 'Latin America', 'China', 'India', 'EU', 'USA']).set_index('Year')
    self.ht = helpertables.HelperTables(ac=self.ac,
                                        ref_datapoints=ht_ref_datapoints, pds_datapoints=ht_pds_datapoints,
                                        ref_adoption_limits=ref_tam_per_region, pds_adoption_limits=pds_tam_per_region,
                                        pds_adoption_data_per_region=self.ad.adoption_data_per_region(),
                                        pds_adoption_trend_per_region=self.ad.adoption_trend_per_region(),
                                        pds_adoption_is_single_source=self.ad.adoption_is_single_source())

    self.ef = emissionsfactors.ElectricityGenOnGrid(ac=self.ac)

    self.ua = unitadoption.UnitAdoption(ac=self.ac, datadir=datadir,
        ref_tam_per_region=ref_tam_per_region, pds_tam_per_region=pds_tam_per_region,
        soln_ref_funits_adopted=self.ht.soln_ref_funits_adopted(),
        soln_pds_funits_adopted=self.ht.soln_pds_funits_adopted(),
        bug_cfunits_double_count=True)
    soln_pds_tot_iunits_reqd = self.ua.soln_pds_tot_iunits_reqd()
    soln_ref_tot_iunits_reqd = self.ua.soln_ref_tot_iunits_reqd()
    conv_ref_tot_iunits = self.ua.conv_ref_tot_iunits()
    soln_net_annual_funits_adopted=self.ua.soln_net_annual_funits_adopted()

    self.fc = firstcost.FirstCost(ac=self.ac, pds_learning_increase_mult=2,
                                  ref_learning_increase_mult=2, conv_learning_increase_mult=2,
                                  soln_pds_tot_iunits_reqd=soln_pds_tot_iunits_reqd,
                                  soln_ref_tot_iunits_reqd=soln_ref_tot_iunits_reqd,
                                  conv_ref_tot_iunits=conv_ref_tot_iunits,
                                  soln_pds_new_iunits_reqd=self.ua.soln_pds_new_iunits_reqd(),
                                  soln_ref_new_iunits_reqd=self.ua.soln_ref_new_iunits_reqd(),
                                  conv_ref_new_iunits=self.ua.conv_ref_new_iunits(),
                                  fc_convert_iunit_factor=rrs.TERAWATT_TO_KILOWATT)

    self.oc = operatingcost.OperatingCost(ac=self.ac,
        soln_net_annual_funits_adopted=soln_net_annual_funits_adopted,
        soln_pds_tot_iunits_reqd=soln_pds_tot_iunits_reqd,
        soln_ref_tot_iunits_reqd=soln_ref_tot_iunits_reqd,
        conv_ref_annual_tot_iunits=self.ua.conv_ref_annual_tot_iunits(),
        soln_pds_annual_world_first_cost=self.fc.soln_pds_annual_world_first_cost(),
        soln_ref_annual_world_first_cost=self.fc.soln_ref_annual_world_first_cost(),
        conv_ref_annual_world_first_cost=self.fc.conv_ref_annual_world_first_cost(),
        single_iunit_purchase_year=2017,
        soln_pds_install_cost_per_iunit=self.fc.soln_pds_install_cost_per_iunit(),
        conv_ref_install_cost_per_iunit=self.fc.conv_ref_install_cost_per_iunit(),
        conversion_factor=rrs.TERAWATT_TO_KILOWATT)

    self.c4 = ch4calcs.CH4Calcs(ac=self.ac,
        soln_net_annual_funits_adopted=soln_net_annual_funits_adopted)
    self.c2 = co2calcs.CO2Calcs(ac=self.ac,
                                ch4_ppb_calculator=self.c4.ch4_ppb_calculator(),
                                soln_pds_net_grid_electricity_units_saved=self.ua.soln_pds_net_grid_electricity_units_saved(),
                                soln_pds_net_grid_electricity_units_used=self.ua.soln_pds_net_grid_electricity_units_used(),
                                soln_pds_direct_co2_emissions_saved=self.ua.soln_pds_direct_co2_emissions_saved(),
                                soln_pds_direct_ch4_co2_emissions_saved=self.ua.soln_pds_direct_ch4_co2_emissions_saved(),
                                soln_pds_direct_n2o_co2_emissions_saved=self.ua.soln_pds_direct_n2o_co2_emissions_saved(),
                                soln_pds_new_iunits_reqd=self.ua.soln_pds_new_iunits_reqd(),
                                soln_ref_new_iunits_reqd=self.ua.soln_ref_new_iunits_reqd(),
                                conv_ref_new_iunits=self.ua.conv_ref_new_iunits(),
                                conv_ref_grid_CO2_per_KWh=self.ef.conv_ref_grid_CO2_per_KWh(),
                                conv_ref_grid_CO2eq_per_KWh=self.ef.conv_ref_grid_CO2eq_per_KWh(),
                                soln_net_annual_funits_adopted=soln_net_annual_funits_adopted,
                                fuel_in_liters=False)

    self.VMAs = []
