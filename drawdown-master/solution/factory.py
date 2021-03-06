"""Return objects for solutions."""

from solution import afforestation
from solution import airplanes
from solution import altcement
from solution import bikeinfrastructure
from solution import bamboo
from solution import biochar
from solution import biogas
from solution import biomass
from solution import bioplastic
from solution import buildingautomation
from solution import carpooling
from solution import cars
from solution import composting
from solution import concentratedsolar
from solution import conservationagriculture
from solution import coolroofs
from solution import districtheating
from solution import electricbikes
from solution import electricvehicles
from solution import farmlandrestoration
from solution import forestprotection
from solution import geothermal
from solution import greenroofs
from solution import heatpumps
from solution import highspeedrail
from solution import improvedcookstoves
from solution import improvedrice
from solution import indigenouspeoplesland
from solution import instreamhydro
from solution import insulation
from solution import irrigationefficiency
from solution import landfillmethane
from solution import leds_commercial
from solution import leds_residential
from solution import managedgrazing
from solution import masstransit
from solution import microwind
from solution import multistrataagroforestry
from solution import nuclear
from solution import nutrientmanagement
from solution import offshorewind
from solution import onshorewind
from solution import peatlands
from solution import perennialbioenergy
from solution import recycledpaper
from solution import refrigerants
from solution import regenerativeagriculture
from solution import riceintensification
from solution import ships
from solution import silvopasture
from solution import smartglass
from solution import smartthermostats
from solution import solarhotwater
from solution import solarpvroof
from solution import solarpvutil
from solution import telepresence
from solution import treeintercropping
from solution import tropicalforests
from solution import tropicaltreestaples
from solution import trains
from solution import trucks
from solution import walkablecities
from solution import waterdistribution
from solution import waterefficiency
from solution import waveandtidal
from solution import womensmallholders

def all_solutions_scenarios():
    everything = {}
    everything['afforestation'] = (afforestation.Afforestation, list(afforestation.scenarios.keys()))
    everything['airplanes'] = (airplanes.Airplanes, list(airplanes.scenarios.keys()))
    everything['altcement'] = (altcement.AlternativeCement, list(altcement.scenarios.keys()))
    everything['bikeinfrastructure'] = (bikeinfrastructure.BikeInfrastructure,
            list(bikeinfrastructure.scenarios.keys()))
    everything['bamboo'] = (bamboo.Bamboo, list(bamboo.scenarios.keys()))
    everything['biochar'] = (biochar.Biochar, list(biochar.scenarios.keys()))
    everything['biogas'] = (biogas.Biogas, list(biogas.scenarios.keys()))
    everything['biomass'] = (biomass.Biomass, list(biomass.scenarios.keys()))
    everything['bioplastic'] = (bioplastic.Bioplastic, list(bioplastic.scenarios.keys()))
    everything['buildingautomation'] = (buildingautomation.BuildingAutomationSystems,
            list(buildingautomation.scenarios.keys()))
    everything['carpooling'] = (carpooling.Carpooling, list(carpooling.scenarios.keys()))
    everything['cars'] = (cars.Cars, list(cars.scenarios.keys()))
    everything['composting'] = (composting.Composting, list(composting.scenarios.keys()))
    everything['concentratedsolar'] = (concentratedsolar.ConcentratedSolar,
            list(concentratedsolar.scenarios.keys()))
    everything['conservationagriculture'] = (conservationagriculture.ConservationAgriculture,
            list(conservationagriculture.scenarios.keys()))
    everything['coolroofs'] = (coolroofs.CoolRoofs, list(coolroofs.scenarios.keys()))
    everything['districtheating'] = (districtheating.DistrictHeating,
            list(districtheating.scenarios.keys()))
    everything['electricbikes'] = (electricbikes.ElectricBicycles,
            list(electricbikes.scenarios.keys()))
    everything['electricvehicles'] = (electricvehicles.ElectricVehicles,
            list(electricvehicles.scenarios.keys()))
    everything['farmlandrestoration'] = (farmlandrestoration.FarmlandRestoration,
            list(farmlandrestoration.scenarios.keys()))
    everything['forestprotection'] = (forestprotection.ForestProtection,
            list(forestprotection.scenarios.keys()))
    everything['geothermal'] = (geothermal.Geothermal, list(geothermal.scenarios.keys()))
    everything['greenroofs'] = (greenroofs.GreenRoofs, list(greenroofs.scenarios.keys()))
    everything['heatpumps'] = (heatpumps.HeatPumps, list(heatpumps.scenarios.keys()))
    everything['highspeedrail'] = (highspeedrail.HighSpeedRail,
            list(highspeedrail.scenarios.keys()))
    everything['improvedcookstoves'] = (improvedcookstoves.ImprovedCookStoves,
            list(improvedcookstoves.scenarios.keys()))
    everything['improvedrice'] = (improvedrice.ImprovedRice, list(improvedrice.scenarios.keys()))
    everything['indigenouspeoplesland'] = (indigenouspeoplesland.IndigenousPeoplesLand,
            list(indigenouspeoplesland.scenarios.keys()))
    everything['instreamhydro'] = (instreamhydro.InstreamHydro,
            list(instreamhydro.scenarios.keys()))
    everything['insulation'] = (insulation.Insulation, list(insulation.scenarios.keys()))
    everything['irrigationefficiency'] = (irrigationefficiency.IrrigationEfficiency,
            list(irrigationefficiency.scenarios.keys()))
    everything['landfillmethane'] = (landfillmethane.LandfillMethane,
            list(landfillmethane.scenarios.keys()))
    everything['leds_commercial'] = (leds_commercial.LEDCommercialLighting,
            list(leds_commercial.scenarios.keys()))
    everything['leds_residential'] = (leds_residential.ResidentialLEDLighting,
            list(leds_residential.scenarios.keys()))
    everything['masstransit'] = (masstransit.MassTransit, list(masstransit.scenarios.keys()))
    everything['managedgrazing'] = (managedgrazing.ManagedGrazing,
            list(managedgrazing.scenarios.keys()))
    everything['microwind'] = (microwind.MicroWind, list(microwind.scenarios.keys()))
    everything['multistrataagroforestry'] = (multistrataagroforestry.MultistrataAgroforestry,
            list(multistrataagroforestry.scenarios.keys()))
    everything['nuclear'] = (nuclear.Nuclear, list(nuclear.scenarios.keys()))
    everything['nutrientmanagement'] = (nutrientmanagement.NutrientManagement,
            list(nutrientmanagement.scenarios.keys()))
    everything['offshorewind'] = (offshorewind.OffshoreWind, list(offshorewind.scenarios.keys()))
    everything['onshorewind'] = (onshorewind.OnshoreWind, list(onshorewind.scenarios.keys()))
    everything['peatlands'] = (peatlands.Peatlands, list(peatlands.scenarios.keys()))
    everything['perennialbioenergy'] = (perennialbioenergy.PerennialBioenergy,
            list(perennialbioenergy.scenarios.keys()))
    everything['recycledpaper'] = (recycledpaper.RecycledPaper,
            list(recycledpaper.scenarios.keys()))
    everything['refrigerants'] = (refrigerants.RefrigerantManagement,
            list(refrigerants.scenarios.keys()))
    everything['regenerativeagriculture'] = (regenerativeagriculture.RegenerativeAgriculture,
            list(regenerativeagriculture.scenarios.keys()))
    everything['riceintensification'] = (riceintensification.RiceIntensification,
            list(riceintensification.scenarios.keys()))
    everything['ships'] = (ships.Ships, list(ships.scenarios.keys()))
    everything['silvopasture'] = (silvopasture.Silvopasture, list(silvopasture.scenarios.keys()))
    everything['smartglass'] = (smartglass.SmartGlass, list(smartglass.scenarios.keys()))
    everything['smartthermostats'] = (smartthermostats.SmartThermostats,
            list(smartthermostats.scenarios.keys()))
    everything['solarhotwater'] = (solarhotwater.SolarHotWater,
            list(solarhotwater.scenarios.keys()))
    everything['solarpvroof'] = (solarpvroof.SolarPVRoof, list(solarpvroof.scenarios.keys()))
    everything['solarpvutil'] = (solarpvutil.SolarPVUtil, list(solarpvutil.scenarios.keys()))
    everything['telepresence'] = (telepresence.Telepresence, list(telepresence.scenarios.keys()))
    everything['treeintercropping'] = (treeintercropping.TreeIntercropping,
            list(treeintercropping.scenarios.keys()))
    everything['tropicalforests'] = (tropicalforests.TropicalForests,
            list(tropicalforests.scenarios.keys()))
    everything['tropicaltreestaples'] = (tropicaltreestaples.TropicalTreeStaples,
            list(tropicaltreestaples.scenarios.keys()))
    everything['trains'] = (trains.TrainFuelEfficiency, list(trains.scenarios.keys()))
    everything['trucks'] = (trucks.Trucks, list(trucks.scenarios.keys()))
    everything['walkablecities'] = (walkablecities.WalkableCities,
            list(walkablecities.scenarios.keys()))
    everything['waterdistribution'] = (waterdistribution.WaterDistribution,
            list(waterdistribution.scenarios.keys()))
    everything['waterefficiency'] = (waterefficiency.WaterEfficiencyMeasures,
            list(waterefficiency.scenarios.keys()))
    everything['waveandtidal'] = (waveandtidal.WaveAndTidal, list(waveandtidal.scenarios.keys()))
    everything['womensmallholders'] = (womensmallholders.WomenSmallholders,
            list(womensmallholders.scenarios.keys()))
    return everything
