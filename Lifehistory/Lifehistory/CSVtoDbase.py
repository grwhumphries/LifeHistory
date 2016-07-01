import csv
from app.models import Species, Traits

dataReader = csv.reader(open("C:/LifeHistory/Lifehistory/Seabirds-edited.csv"), delimiter=',', quotechar='"')

count = 1
for row in dataReader:
    if row[0] != 'order':
        print row 
        species = Species()
        species.order=row[0]
        species.family=row[1]
        species.genus=row[2]
        species.species=row[3]
        species.species_id=row[4]
        species.synonyms=row[5]
        species.common_name_1=row[6]
        species.common_name_2=row[7]
        species.common_name_3=row[8]
        species.common_name_4=row[9]
        species.common_name_5=row[10]
        species.common_name_6=row[11]
        species.iucn_status=row[12]
        species.red_list_criteria=row[13]
        species.year_assessed=row[14]
        species.population_trend=row[15]
        species.breeding_dist=row[24]
        species.nest_locations=row[25]
        species.hatchling_type=row[31]
        species.foraging_distance=row[52]
        species.coloniality=row[65]
         
        species.save()   


        traits = Traits()
        traits.spec = Species.objects.get(fid = count)
        
        traits.female_mass_mean=row[16]
        traits.female_mass_upper=row[17]
        traits.female_mass_lower=row[18]
        traits.female_mass_uncertainty=row[19]
        traits.male_mass_mean=row[20]
        traits.male_mass_lower=row[21]
        traits.male_mass_upper=row[22]
        traits.male_mass_uncertainty=row[23]

        traits.clutch_size_mean=row[26]
        traits.clutch_size_lower=row[27]
        traits.cluth_size_upper=row[28]
        traits.clutch_size_uncertainty=row[29]
        traits.clutch_interval=row[30]

        traits.incubation_mean=row[32]
        traits.incubation_period_lower=row[33]
        traits.incubtaion_period_upper=row[34]
        traits.incubation_period_uncertainty=row[35]
        traits.fledging_period_mean=row[36]
        traits.fledging_period_lower=row[37]
        traits.fledging_period_upper=row[38]
        traits.fledging_period_uncertainty=row[39]
        traits.max_growth_mean=row[40]
        traits.max_growth_lower=row[41]
        traits.max_growth_upper=row[42]
        traits.max_growth_uncertainty=row[43]
        traits.post_fledge_care_mean=row[44]
        traits.post_fledge_care_lower=row[45]
        traits.post_fledge_care_upper=row[46]
        traits.post_fledge_care_uncertainty=row[47]
        traits.age_first_breed_mean=row[48]
        traits.age_first_breed_lower=row[49]
        traits.age_first_breed_upper=row[50]
        traits.age_first_breed_uncertainty=row[51]

        traits.wingspan_mean=row[53]
        traits.wingspan_lower=row[54]
        traits.wingspan_upper=row[55]
        traits.wingspan_uncertainty=row[56]
        traits.max_age_mean=row[57]
        traits.max_age_lower=row[58]
        traits.max_age_upper=row[59]
        traits.max_age_uncertainty=row[60]
        traits.annual_survival_mean=row[61]
        traits.annual_survival_lower=row[62]
        traits.annual_survival_upper=row[63]
        traits.annual_survival_uncertainty=row[64]

        traits.citation=row[66]
        traits.save()
        del traits
        count = count+1







