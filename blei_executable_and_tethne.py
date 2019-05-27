import os
import csv
import tethne


### GENERATE CONFERENCES LIST AND YEARS ###
def make_csv(time_stamps,type):

    try:
        #Get conferences names to be analized.
        conference = 'tourism'

        #time_stamps = ['Jan','Feb', 'Mar','Apr','May','Jun','Jul','Aug','Sep','Oct', 'Nov', 'Dec']
        #time_stamps = ['May']
        #type='Month'


        #Create file to export
        with open('OutputDTM.csv', 'wb') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            #Write header
            writer.writerow(['Conference', 'TopicID', 'Word',type , 'Probability'])


            #Make DTM
            os.system('dtm-win64.exe ./main --ntopics=3 --mode=fit --rng_seed=0 --initialize_lda=true --corpus_prefix=data/' + conference + '/foo --outname=data/' + conference + '/output --top_chain_var=0.9 --alpha=0.01 --lda_sequence_min_iter=6 --lda_sequence_max_iter=20 --lda_max_em_iter=20')

            #Import to tethne
            dtm = tethne.model.corpus.dtmmodel.from_gerrish('data/' + conference + '/output/','data/' + conference + '/metadata.dat','data/' + conference + '/vocabulary.dat')

            print("=================================================================")
            print(dtm)



            for i in range(3):
                arr = dtm.topic_evolution(i,10)

                for key in arr[1].keys():
                    for month_i in range(len(time_stamps)):

                        writer.writerow([conference, i, key, (time_stamps[month_i]), arr[1][key][month_i]])
        return True
    except Exception:
        return False