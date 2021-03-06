"""Solar Hot Water solution model.
   Excel filename: Drawdown-Solar Hot Water_RRS_v1.1_21Nov2018_PUBLIC.xlsm
"""

import pathlib

import numpy as np
import pandas as pd

from model import adoptiondata
from model import advanced_controls
from model import ch4calcs
from model import co2calcs
from model import customadoption
from model import emissionsfactors
from model import firstcost
from model import helpertables
from model import operatingcost
from model import s_curve
from model import unitadoption
from model import vma
from model.advanced_controls import SOLUTION_CATEGORY

from model import tam
from solution import rrs

DATADIR = str(pathlib.Path(__file__).parents[2].joinpath('data'))
THISDIR = pathlib.Path(__file__).parents[0]
VMAs = vma.generate_vma_dict(THISDIR.joinpath('vma_data'))

REGIONS = ['World', 'OECD90', 'Eastern Europe', 'Asia (Sans Japan)', 'Middle East and Africa',
           'Latin America', 'China', 'India', 'EU', 'USA']

scenarios = {
  'PDS1-25p2050-Low of Custom Scen. (Book Ed.1)': advanced_controls.AdvancedControls(
      # Several custom scenarios (and some developed by other sources) were recorded and
      # statistically combined to create low, medium and high meta-scenarios (based on
      # -1, 0 and +1 standard deviations from the mean). The low was used for this
      # scenario. We assume that solar water heating would replace only natural gas,
      # oil, coal and electricity heaters (that is, no biomass or commercial heat). This
      # scenario uses inputs calculated for the Drawdown book edition 1, some of which
      # have been updated.

      # general
      report_start_year=2020, report_end_year=2050, 

      # adoption
      soln_ref_adoption_basis='Default', 
      soln_ref_adoption_regional_data=False, soln_pds_adoption_regional_data=False, 
      soln_pds_adoption_basis='Fully Customized PDS', 
      soln_pds_adoption_custom_name='Low of All Custom PDS Scenarios', 
      source_until_2014='ALL SOURCES', 
      ref_source_post_2014='IEA 4DS (2016), Residential & Commercial Water Heating', 
      pds_source_post_2014='Drawdown TAM: PDS1 - post-Low-Flow', 
      pds_base_adoption=[('World', 335.463), ('OECD90', 56.493), ('Eastern Europe', 2.374), ('Asia (Sans Japan)', 240.305), ('Middle East and Africa', 9.948), ('Latin America', 9.113), ('China', 231.838), ('India', 6.4350000000000005), ('EU', 23.777), ('USA', 17.233)], 
      pds_adoption_final_percentage=[('World', 0.0), ('OECD90', 0.0), ('Eastern Europe', 0.0), ('Asia (Sans Japan)', 0.0), ('Middle East and Africa', 0.0), ('Latin America', 0.0), ('China', 0.0), ('India', 0.0), ('EU', 0.0), ('USA', 0.0)], 

      # financial
      pds_2014_cost=1199.8861226016184, ref_2014_cost=1199.8861226016184, 
      conv_2014_cost=0.0, 
      soln_first_cost_efficiency_rate=0.036, 
      conv_first_cost_efficiency_rate=0.0, 
      soln_first_cost_below_conv=True, 
      npv_discount_rate=0.04, 
      soln_lifetime_capacity=17129.2410031799, soln_avg_annual_use=856.462050158993, 
      conv_lifetime_capacity=1.0, conv_avg_annual_use=1.0, 

      soln_var_oper_cost_per_funit=0.047, soln_fuel_cost_per_funit=0.0, 
      soln_fixed_oper_cost_per_iunit=0.0, 
      conv_var_oper_cost_per_funit=0.0, conv_fuel_cost_per_funit=0.0795, 
      conv_fixed_oper_cost_per_iunit=0.0, 

      # emissions
      ch4_is_co2eq=False, n2o_is_co2eq=False, 
      co2eq_conversion_source='AR5 with feedback', 
      soln_indirect_co2_per_iunit=0.0, 
      conv_indirect_co2_per_unit=0.0, 
      conv_indirect_co2_is_iunits=False, 
      ch4_co2_per_twh=0.0, n2o_co2_per_twh=0.0, 

      soln_energy_efficiency_factor=1.0, 
      soln_annual_energy_used=0.0, conv_annual_energy_used=0.11587780896849142, 
      conv_fuel_consumed_per_funit=2483.195162856096, soln_fuel_efficiency_factor=1.0, 
      conv_fuel_emissions_factor=69.71707858620789, soln_fuel_emissions_factor=0.0, 

      emissions_grid_source='Meta-Analysis', emissions_grid_range='Mean', 
      emissions_use_co2eq=True, 
      conv_emissions_per_funit=0.0, soln_emissions_per_funit=0.0, 

    ),
  'PDS2-44p2050-Mean of Custom Scen. (Book Ed.1)': advanced_controls.AdvancedControls(
      # Several custom scenarios (and some developed by other sources) were recorded and
      # statistically combined to create low, medium and high meta-scenarios (based on
      # -1, 0 and +1 standard deviations from the mean). The mean was used for this
      # scenario. We assume that solar water heating would replace only natural gas,
      # oil, coal and electricity heaters (that is, no biomass or commercial heat). This
      # scenario uses inputs calculated for the Drawdown book edition 1, some of which
      # have been updated.

      # general
      report_start_year=2020, report_end_year=2050, 

      # adoption
      soln_ref_adoption_basis='Default', 
      soln_ref_adoption_regional_data=False, soln_pds_adoption_regional_data=False, 
      soln_pds_adoption_basis='Fully Customized PDS', 
      soln_pds_adoption_custom_name='Average of All Custom PDS Scenarios', 
      source_until_2014='ALL SOURCES', 
      ref_source_post_2014='IEA 4DS (2016), Residential & Commercial Water Heating', 
      pds_source_post_2014='Drawdown TAM: PDS2 - post-Low-Flow', 
      pds_base_adoption=[('World', 335.463), ('OECD90', 56.493), ('Eastern Europe', 2.374), ('Asia (Sans Japan)', 240.305), ('Middle East and Africa', 9.948), ('Latin America', 9.113), ('China', 231.838), ('India', 6.4350000000000005), ('EU', 23.777), ('USA', 17.233)], 
      pds_adoption_final_percentage=[('World', 0.0), ('OECD90', 0.0), ('Eastern Europe', 0.0), ('Asia (Sans Japan)', 0.0), ('Middle East and Africa', 0.0), ('Latin America', 0.0), ('China', 0.0), ('India', 0.0), ('EU', 0.0), ('USA', 0.0)], 

      # financial
      pds_2014_cost=1199.8861226016184, ref_2014_cost=1199.8861226016184, 
      conv_2014_cost=0.0, 
      soln_first_cost_efficiency_rate=0.036, 
      conv_first_cost_efficiency_rate=0.0, 
      soln_first_cost_below_conv=True, 
      npv_discount_rate=0.04, 
      soln_lifetime_capacity=17129.2410031799, soln_avg_annual_use=856.462050158993, 
      conv_lifetime_capacity=1.0, conv_avg_annual_use=1.0, 

      soln_var_oper_cost_per_funit=0.047, soln_fuel_cost_per_funit=0.0, 
      soln_fixed_oper_cost_per_iunit=0.0, 
      conv_var_oper_cost_per_funit=0.0, conv_fuel_cost_per_funit=0.0795, 
      conv_fixed_oper_cost_per_iunit=0.0, 

      # emissions
      ch4_is_co2eq=False, n2o_is_co2eq=False, 
      co2eq_conversion_source='AR5 with feedback', 
      soln_indirect_co2_per_iunit=0.0, 
      conv_indirect_co2_per_unit=0.0, 
      conv_indirect_co2_is_iunits=False, 
      ch4_co2_per_twh=0.0, n2o_co2_per_twh=0.0, 

      soln_energy_efficiency_factor=1.0, 
      soln_annual_energy_used=0.0, conv_annual_energy_used=0.11587780896849142, 
      conv_fuel_consumed_per_funit=2483.195162856096, soln_fuel_efficiency_factor=1.0, 
      conv_fuel_emissions_factor=69.71707858620789, soln_fuel_emissions_factor=0.0, 

      emissions_grid_source='Meta-Analysis', emissions_grid_range='Mean', 
      emissions_use_co2eq=True, 
      conv_emissions_per_funit=0.0, soln_emissions_per_funit=0.0, 

    ),
  'PDS3-62p2050-High of Custom Scen. (Book Ed.1)': advanced_controls.AdvancedControls(
      # Several custom scenarios (and some developed by other sources) were recorded and
      # statistically combined to create low, medium and high meta-scenarios (based on
      # -1, 0 and +1 standard deviations from the mean). The high was used for this
      # scenario. We assume that solar water heating would replace only natural gas,
      # oil, coal and electricity heaters (that is, no biomass or commercial heat). This
      # scenario uses inputs calculated for the Drawdown book edition 1, some of which
      # have been updated.

      # general
      report_start_year=2020, report_end_year=2050, 

      # adoption
      soln_ref_adoption_basis='Default', 
      soln_ref_adoption_regional_data=False, soln_pds_adoption_regional_data=False, 
      soln_pds_adoption_basis='Fully Customized PDS', 
      soln_pds_adoption_custom_name='High of All Custom PDS Scenarios', 
      source_until_2014='ALL SOURCES', 
      ref_source_post_2014='IEA 4DS (2016), Residential & Commercial Water Heating', 
      pds_source_post_2014='Drawdown TAM: PDS3 - post-Low-Flow', 
      pds_base_adoption=[('World', 335.463), ('OECD90', 56.493), ('Eastern Europe', 2.374), ('Asia (Sans Japan)', 240.305), ('Middle East and Africa', 9.948), ('Latin America', 9.113), ('China', 231.838), ('India', 6.4350000000000005), ('EU', 23.777), ('USA', 17.233)], 
      pds_adoption_final_percentage=[('World', 0.0), ('OECD90', 0.0), ('Eastern Europe', 0.0), ('Asia (Sans Japan)', 0.0), ('Middle East and Africa', 0.0), ('Latin America', 0.0), ('China', 0.0), ('India', 0.0), ('EU', 0.0), ('USA', 0.0)], 

      # financial
      pds_2014_cost=1199.8861226016184, ref_2014_cost=1199.8861226016184, 
      conv_2014_cost=0.0, 
      soln_first_cost_efficiency_rate=0.036, 
      conv_first_cost_efficiency_rate=0.0, 
      soln_first_cost_below_conv=True, 
      npv_discount_rate=0.04, 
      soln_lifetime_capacity=17129.2410031799, soln_avg_annual_use=856.462050158993, 
      conv_lifetime_capacity=1.0, conv_avg_annual_use=1.0, 

      soln_var_oper_cost_per_funit=0.047, soln_fuel_cost_per_funit=0.0, 
      soln_fixed_oper_cost_per_iunit=0.0, 
      conv_var_oper_cost_per_funit=0.0, conv_fuel_cost_per_funit=0.0795, 
      conv_fixed_oper_cost_per_iunit=0.0, 

      # emissions
      ch4_is_co2eq=False, n2o_is_co2eq=False, 
      co2eq_conversion_source='AR5 with feedback', 
      soln_indirect_co2_per_iunit=0.0, 
      conv_indirect_co2_per_unit=0.0, 
      conv_indirect_co2_is_iunits=False, 
      ch4_co2_per_twh=0.0, n2o_co2_per_twh=0.0, 

      soln_energy_efficiency_factor=1.0, 
      soln_annual_energy_used=0.0, conv_annual_energy_used=0.11587780896849142, 
      conv_fuel_consumed_per_funit=2483.195162856096, soln_fuel_efficiency_factor=1.0, 
      conv_fuel_emissions_factor=69.71707858620789, soln_fuel_emissions_factor=0.0, 

      emissions_grid_source='Meta-Analysis', emissions_grid_range='Mean', 
      emissions_use_co2eq=True, 
      conv_emissions_per_funit=0.0, soln_emissions_per_funit=0.0, 

    ),
}

class SolarHotWater:
  name = 'Solar Hot Water'
  units = {
    "implementation unit": "TW",
    "functional unit": "TWh(th)",
    "first cost": "US$B",
    "operating cost": "US$B",
  }

  def __init__(self, scenario=None):
    if scenario is None:
      scenario = 'PDS1-25p2050-Low of Custom Scen. (Book Ed.1)'
    self.scenario = scenario
    self.ac = scenarios[scenario]

    # TAM
    tamconfig_list = [
      ['param', 'World', 'PDS World', 'OECD90', 'Eastern Europe', 'Asia (Sans Japan)',
       'Middle East and Africa', 'Latin America', 'China', 'India', 'EU', 'USA'],
      ['source_until_2014', self.ac.source_until_2014, self.ac.source_until_2014,
       'ALL SOURCES', 'ALL SOURCES', 'ALL SOURCES', 'ALL SOURCES', 'ALL SOURCES', 'ALL SOURCES',
       'ALL SOURCES', 'ALL SOURCES', 'ALL SOURCES'],
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
    tamconfig = pd.DataFrame(tamconfig_list[1:], columns=tamconfig_list[0], dtype=np.object).set_index('param')
    tam_ref_data_sources = {
      'Baseline Cases': {
          'Custom calculated from (GBPN, Urge-Vorsatz Factored by IEA Building  Data)': THISDIR.joinpath('tam', 'tam_Custom_calculated_from_GBPN_UrgeVorsatz_Factored_by_IEA_Building_Data.csv'),
          'IEA 6DS (2016), Residential & Commercial Water Heating': THISDIR.joinpath('tam', 'tam_IEA_6DS_2016_Residential_Commercial_Water_Heating.csv'),
          'GBPN Energy for water heating, Urban & Rural / All buildings, All Vintages, Frozen efficiency (Water Heating Thermal energy use in TWHth)': THISDIR.joinpath('tam', 'tam_GBPN_Energy_for_water_heating_Urban_Rural_All_buildings_All_Vintages_Frozen_efficiency_W_e86b69eb.csv'),
      },
      'Conservative Cases': {
          'Custom calculated from (GBPN and Urge-Vorsatz)': THISDIR.joinpath('tam', 'tam_Custom_calculated_from_GBPN_and_UrgeVorsatz.csv'),
          'IEA 4DS (2016), Residential & Commercial Water Heating': THISDIR.joinpath('tam', 'tam_IEA_4DS_2016_Residential_Commercial_Water_Heating.csv'),
      },
      'Region: OECD90': {
        'Baseline Cases': {
          'Custom calculated from (GBPN, Urge-Vorsatz Factored by IEA Building  Data)': THISDIR.joinpath('tam', 'tam_Custom_calculated_from_GBPN_UrgeVorsatz_Factored_by_IEA_Building_Data.csv'),
          'Custom calculated from (GBPN and Urge-Vorsatz)': THISDIR.joinpath('tam', 'tam_Custom_calculated_from_GBPN_and_UrgeVorsatz.csv'),
          'GBPN Energy for water heating, Urban & Rural / All buildings, All Vintages, Frozen efficiency (Water Heating Thermal energy use in TWHth)': THISDIR.joinpath('tam', 'tam_GBPN_Energy_for_water_heating_Urban_Rural_All_buildings_All_Vintages_Frozen_efficiency_W_e86b69eb.csv'),
        },
      },
      'Region: Eastern Europe': {
        'Baseline Cases': {
          'Custom calculated from (GBPN, Urge-Vorsatz Factored by IEA Building  Data)': THISDIR.joinpath('tam', 'tam_Custom_calculated_from_GBPN_UrgeVorsatz_Factored_by_IEA_Building_Data.csv'),
          'Custom calculated from (GBPN and Urge-Vorsatz)': THISDIR.joinpath('tam', 'tam_Custom_calculated_from_GBPN_and_UrgeVorsatz.csv'),
          'GBPN Energy for water heating, Urban & Rural / All buildings, All Vintages, Frozen efficiency (Water Heating Thermal energy use in TWHth)': THISDIR.joinpath('tam', 'tam_GBPN_Energy_for_water_heating_Urban_Rural_All_buildings_All_Vintages_Frozen_efficiency_W_e86b69eb.csv'),
        },
      },
      'Region: Asia (Sans Japan)': {
        'Baseline Cases': {
          'Custom calculated from (GBPN, Urge-Vorsatz Factored by IEA Building  Data)': THISDIR.joinpath('tam', 'tam_Custom_calculated_from_GBPN_UrgeVorsatz_Factored_by_IEA_Building_Data.csv'),
          'Custom calculated from (GBPN and Urge-Vorsatz)': THISDIR.joinpath('tam', 'tam_Custom_calculated_from_GBPN_and_UrgeVorsatz.csv'),
          'GBPN Energy for water heating, Urban & Rural / All buildings, All Vintages, Frozen efficiency (Water Heating Thermal energy use in TWHth)': THISDIR.joinpath('tam', 'tam_GBPN_Energy_for_water_heating_Urban_Rural_All_buildings_All_Vintages_Frozen_efficiency_W_e86b69eb.csv'),
        },
      },
    }
    tam_pds_data_sources = {
      'Baseline Cases': {
          'Drawdown TAM: PDS1 - post-Low-Flow': THISDIR.joinpath('tam', 'tam_pds_Drawdown_TAM_PDS1_postLowFlow.csv'),
      },
      'Conservative Cases': {
          'Drawdown TAM: PDS2 - post-Low-Flow': THISDIR.joinpath('tam', 'tam_pds_Drawdown_TAM_PDS2_postLowFlow.csv'),
      },
      'Ambitious Cases': {
          'Drawdown TAM: PDS3 - post-Low-Flow': THISDIR.joinpath('tam', 'tam_pds_Drawdown_TAM_PDS3_postLowFlow.csv'),
      },
    }
    self.tm = tam.TAM(tamconfig=tamconfig, tam_ref_data_sources=tam_ref_data_sources,
      tam_pds_data_sources=tam_pds_data_sources)
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
    adconfig = pd.DataFrame(adconfig_list[1:], columns=adconfig_list[0], dtype=np.object).set_index('param')
    ad_data_sources = {
      'Conservative Cases': {
          'IEA (2012) Technology Roadmap Solar Heating and Cooling - Cons': THISDIR.joinpath('ad', 'ad_IEA_2012_Technology_Roadmap_Solar_Heating_and_Cooling_Cons.csv'),
      },
      'Ambitious Cases': {
          'Solar Heat Worldwide http://www.iea-shc.org/solar-heat-worldwide': THISDIR.joinpath('ad', 'ad_Solar_Heat_Worldwide_httpwww_ieashc_orgsolarheatworldwide.csv'),
      },
    }
    self.ad = adoptiondata.AdoptionData(ac=self.ac, data_sources=ad_data_sources,
        adconfig=adconfig)

    # Custom PDS Data
    ca_pds_data_sources = [
      {'name': 'Conservative, based on IEA 2012', 'include': True,
          'filename': THISDIR.joinpath('ca_pds_data', 'custom_pds_ad_Conservative_based_on_IEA_2012.csv')},
      {'name': 'Aggressive, High Growth, early', 'include': True,
          'filename': THISDIR.joinpath('ca_pds_data', 'custom_pds_ad_Aggressive_High_Growth_early.csv')},
      {'name': 'Aggressive, High Growth, based on IEA', 'include': True,
          'filename': THISDIR.joinpath('ca_pds_data', 'custom_pds_ad_Aggressive_High_Growth_based_on_IEA.csv')},
      {'name': 'Aggressive, High Growth, late', 'include': True,
          'filename': THISDIR.joinpath('ca_pds_data', 'custom_pds_ad_Aggressive_High_Growth_late.csv')},
      {'name': 'Aggressive, V. High Growth, late', 'include': True,
          'filename': THISDIR.joinpath('ca_pds_data', 'custom_pds_ad_Aggressive_V__High_Growth_late.csv')},
      {'name': 'Aggressive, V. High Growth', 'include': True,
          'filename': THISDIR.joinpath('ca_pds_data', 'custom_pds_ad_Aggressive_V__High_Growth.csv')},
      {'name': 'Conservative Growth, late', 'include': True,
          'filename': THISDIR.joinpath('ca_pds_data', 'custom_pds_ad_Conservative_Growth_late.csv')},
      {'name': 'Conservative Growth, early', 'include': True,
          'filename': THISDIR.joinpath('ca_pds_data', 'custom_pds_ad_Conservative_Growth_early.csv')},
      {'name': 'Low Growth', 'include': True,
          'filename': THISDIR.joinpath('ca_pds_data', 'custom_pds_ad_Low_Growth.csv')},
    ]
    self.pds_ca = customadoption.CustomAdoption(data_sources=ca_pds_data_sources,
        soln_adoption_custom_name=self.ac.soln_pds_adoption_custom_name,
        high_sd_mult=1.0, low_sd_mult=1.0,
        total_adoption_limit=pds_tam_per_region)

    ref_adoption_data_per_region = None

    if False:
      # One may wonder why this is here. This file was code generated.
      # This 'if False' allows subsequent conditions to all be elif.
      pass
    elif self.ac.soln_pds_adoption_basis == 'Fully Customized PDS':
      pds_adoption_data_per_region = self.pds_ca.adoption_data_per_region()
      pds_adoption_trend_per_region = self.pds_ca.adoption_trend_per_region()
      pds_adoption_is_single_source = None
    elif self.ac.soln_pds_adoption_basis == 'Existing Adoption Prognostications':
      pds_adoption_data_per_region = self.ad.adoption_data_per_region()
      pds_adoption_trend_per_region = self.ad.adoption_trend_per_region()
      pds_adoption_is_single_source = self.ad.adoption_is_single_source()

    ht_ref_adoption_initial = pd.Series(
      [335.463, 56.493, 2.374, 240.305, 9.948,
       9.113, 231.838, 6.4350000000000005, 23.777, 17.233],
       index=REGIONS)
    ht_ref_adoption_final = ref_tam_per_region.loc[2050] * (ht_ref_adoption_initial / ref_tam_per_region.loc[2014])
    ht_ref_datapoints = pd.DataFrame(columns=REGIONS)
    ht_ref_datapoints.loc[2014] = ht_ref_adoption_initial
    ht_ref_datapoints.loc[2050] = ht_ref_adoption_final.fillna(0.0)
    ht_pds_adoption_initial = ht_ref_adoption_initial
    ht_regions, ht_percentages = zip(*self.ac.pds_adoption_final_percentage)
    ht_pds_adoption_final_percentage = pd.Series(list(ht_percentages), index=list(ht_regions))
    ht_pds_adoption_final = ht_pds_adoption_final_percentage * pds_tam_per_region.loc[2050]
    ht_pds_datapoints = pd.DataFrame(columns=REGIONS)
    ht_pds_datapoints.loc[2014] = ht_pds_adoption_initial
    ht_pds_datapoints.loc[2050] = ht_pds_adoption_final.fillna(0.0)
    self.ht = helpertables.HelperTables(ac=self.ac,
        ref_datapoints=ht_ref_datapoints, pds_datapoints=ht_pds_datapoints,
        pds_adoption_data_per_region=pds_adoption_data_per_region,
        ref_adoption_limits=ref_tam_per_region, pds_adoption_limits=pds_tam_per_region,
        pds_adoption_trend_per_region=pds_adoption_trend_per_region,
        pds_adoption_is_single_source=pds_adoption_is_single_source)

    self.ef = emissionsfactors.ElectricityGenOnGrid(ac=self.ac)

    self.ua = unitadoption.UnitAdoption(ac=self.ac,
        ref_tam_per_region=ref_tam_per_region, pds_tam_per_region=pds_tam_per_region,
        soln_ref_funits_adopted=self.ht.soln_ref_funits_adopted(),
        soln_pds_funits_adopted=self.ht.soln_pds_funits_adopted(),
        repeated_cost_for_iunits=False,
        bug_cfunits_double_count=False)
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
        fc_convert_iunit_factor=1000000000.0)

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
        conversion_factor=1000000000.0)

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

    self.r2s = rrs.RRS(total_energy_demand=ref_tam_per_region.loc[2014, 'World'],
        soln_avg_annual_use=self.ac.soln_avg_annual_use,
        conv_avg_annual_use=self.ac.conv_avg_annual_use)

