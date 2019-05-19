
import pandas as pd
from plotnine import *



def plot(time_stamps,type):

    try:
        # read data
        data = pd.read_csv("OutputDTM.csv")

        #time_stamps = ['May']
        #type='Month'
        value=time_stamps[0]

        if(type=="Month"):
            nudege_x=[0,0,-0.4,0.5,-0.4,0,0.2,0.7,0.2,0.5,0.5,0.9,0.9]
        else:
            nudege_x = [0 for i in time_stamps]


        fig=(
            ggplot(data,aes(x=type,y='Word'))
            + geom_tile(aes(fill = 'Probability'), colour="black",stat = "identity")
            + scale_fill_gradient(low="white", high="blue")

            + facet_wrap('~ TopicID',scales="free_y", ncol=5)
            + geom_text(data.loc[data.loc[:,type]==value],aes(label='Word'), size=9,nudge_x=nudege_x[len(time_stamps)])
            + theme_bw()
            + theme(panel_spacing=.75)
            + theme(panel_grid_major =element_blank(), legend_position="bottom", panel_grid_minor = element_blank())
            + theme(axis_ticks= element_blank(), axis_text_y = element_blank(), axis_title_x = element_blank(), axis_title_y = element_blank(), axis_text_x = element_text(angle=60, vjust=0.1, hjust=0.1, size=5), strip_background = element_blank(), strip_text = element_text(size=7), legend_text = element_text(size=4), legend_title = element_text(size=4), plot_margin = 0.1, legend_margin = -0.6, legend_key_height = 0.4)

        )

        fig

        fig.save(filename="03.png" ,path='./static/',format='png')

        return True
    except Exception:
        return False
