
import re
import PySimpleGUI as sg
from pathlib import Path
import os



os.chdir('/home/michael/Dropbox/dictation')

def getcaptures():
    if Path(filename).is_file():
        with open(filename, "r", encoding='utf-8') as f:
            data = f.read()
            global presenting
            presenting = re.search(("(?<=Illness:)((.|\n)*)(?=Treatment / Therapy)"), data)
            medical = re.search(("(?<=Health History:)((.|\n)*)(?=Psychiatric History and Treatment:)"), data)
            meds = re.search(("(?<=Medications:)((.|\n)*)(?=Clinical Review Of Systems:)"), data)
            psyHx = re.search(("(?<=Psychiatric History and Treatment:)((.|\n)*)(?=Childhood History:)"), data)
            education = re.search(("(?<=Childhood History:)((.|\n)*)(?=Safety Information:)"), data)
            current_status = re.search(("(?<=Additional Personal Information:)((.|\n)*)(?=Family Dynamics:)"), data)
            Family = re.search(("(?<=Additional Personal Information:)((.|\n)*)(?=Family Dynamics:)"), data)
            ROS = re.search(("(?<=Clinical Review Of Systems:)((.|\n)*)(?=Mental Status Examination:)"), data)
            SA = re.search(("(?<=Drug and Alcohol History and Treatment:)((.|\n)*)(?=Additional Personal Information:)"), data)
            SI = re.search(("(?<=Safety Information:)((.|\n)*)(?=Nutrition Information:)"), data)
            orientation = re.search(("(?<=Orientation:)((.|\n)*)(?=Appearance)"), data)
            affect = re.search(("(?<=Affect:)((.|\n)*)(?=Mood)"), data)
            mood = re.search(("(?<=Mood:)((.|\n)*)(?=Orientation)"), data)
            appearance = re.search(("(?<=Appearance:)((.|\n)*)(?=Nutritional)"), data)
            nutrition = re.search(("(?<=Nutritional Habits:)((.|\n)*)(?=Attention / Vigilance / Concentration:)"), data)
            attention = re.search(("(?<=Attention / Vigilance / Concentration:)((.|\n)*)(?=Speech:)"), data)
            speech = re.search(("(?<=Speech:)((.|\n)*)(?=Mental)"), data)
            ROT = re.search(("(?<=Rate of Thoughts:)((.|\n)*)(?=Reasoning)"), data)
            Reasoning = re.search(("(?<=Reasoning:)((.|\n)*)(?=Simple)"), data)
            Calcs = re.search(("(?<=Simple Calculations:)((.|\n)*)(?=Long Term Memory)"), data)
            STM = re.search(("(?<=Short Term Memory:)((.|\n)*)(?=Fund of Knowledge)"), data)
            LTM = re.search(("(?<=Long Term Memory:)((.|\n)*)(?=Short Term Memory)"), data)
            FOK = re.search(("(?<=Fund of Knowledge:)((.|\n)*)(?=Language)"), data)
            Lang = re.search(("(?<=Language:)((.|\n)*)(?=Higher)"), data)
            Judg = re.search(("(?<=Judgment:)((.|\n)*)(?=Insight:)"), data)
            Insight = re.search(("(?<=Insight:)((.|\n)*)(?=Thought Content / Processes:)"), data)
            Hallucinations = re.search(("(?<=Hallucinations:)((.|\n)*)(?=Delusions:)"), data)
            Delusions = re.search(("(?<=Delusions:)((.|\n)*)(?=Associations:)"), data)
            ThoughtContent = re.search(("(?<=Thought Content:)((.|\n)*)(?=Thought Process:)"), data)
            ThoughtProcessses = re.search(("(?<=Thought Process:)((.|\n)*)(?=Risk Assessments:)"), data)


        with open(location, "a") as o:
            o.writelines(presenting.group(0))
            o.writelines(medical.group(0))
            o.writelines(meds.group(0))
            o.writelines(psyHx.group(0))
            o.writelines(education.group(0))
            o.writelines(current_status.group(0))
            o.writelines(Family.group(0))
            o.writelines(ROS.group(0))
            o.writelines("During the course of the clinical interview, time was spent performing a mental status examination. ")
            o.writelines(sal +  " " + firstname + " " + lastname + " was "+ str(orientation.group()).strip() +" to person, place, time, and situation. ")
            o.writelines(s_pro.title() + " endorsed " + str(affect.group()).strip() + " affect. ")
            o.writelines(firstname + "  endorsed " + po_pro + " mood as being " + str(mood.group()).strip()  + ". ")
            o.writelines("When discussing attention, " + s_pro + " endorsed it as being " + str(appearance.group()).strip() + " and appearance and " + str(nutrition.group()).strip() + " nutrition.")
            o.writelines(s_pro.title() + " endorsed " + str(attention.group()).strip() + "attention and " + str(speech.group()).strip() + ".")
            o.writelines(s_pro.title() + " endorsed " + str(ROT.group()).strip() + "appearance and " + str(Reasoning.group()).strip() + ".")
            o.writelines(s_pro.title() + " was able to perform " + str(Calcs.group()).strip() + "calculations such as word rotation and serial sevens. He rated his short term memory as " + str(STM.group()).strip() + " and  his long term memory as " + str(LTM.group()).strip() + ".")
            o.writelines(s_pro.title() + " endorsed fund of knowledge as " + str(FOK.group()).strip() + " compared to his peers. Language appeared " + str(Reasoning.group()).strip() + ". ")
            o.writelines(s_pro.title() + " rated judgement as being " + str(Judg.group()).strip() + " insight as " + str(Insight.group()).strip() + ".")
            o.writelines("When asked about hallucinations, " + po_pro + "stated" + str(Hallucinations.group()).strip() + ". Likewise " + s_pro + " endorsed delusions as" + str(Delusions.group()).strip() + ".")
            o.writelines("When discussing thought content, " + po_pro + "indicated" + str(ThoughtContent.group()).strip() + ". When discussing  thought processes," + s_pro + " indicated "+ str(ThoughtProcessses.group()).strip() + ".")


layout = [
    [sg.Text('Lets get some background data.',justification='center',size=(70,1))],
    [sg.Text('Mr./ Ms/ Dr.', size =(20, 1)), sg.InputText(key='sal', do_not_clear=False)],
    [sg.Text('him or her', size =(20, 1)), sg.InputText(key='po_pro', do_not_clear=False)],
    [sg.Text('he or she', size =(20, 1)), sg.InputText(key='s_pro', do_not_clear=False)],
    [sg.Text('Patient First Name', size =(20, 1)), sg.InputText(key='input_firstname', do_not_clear=False)],
    [sg.Text('Patient Last Name', size =(20, 1)), sg.InputText(key='input_lastname', do_not_clear=False)],
    [sg.Input(key='-INPUT-', do_not_clear=True)],
    [sg.FileBrowse(file_types=(("TXT Files", "*.txt"), ("ALL Files", "*.*")))],
    [sg.Button("Submit")]]

window = sg.Window('BackgroundWriter0.1.6', layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    if event == 'Submit':
            #filename = values['-INPUT-']
            sal = (values['sal'])
            po_pro = (values['po_pro'])
            s_pro = (values['s_pro'])
            firstname = (values['input_firstname'])
            lastname = (values['input_lastname'])
            location = '/home/michael/Dropbox/dictation/'+ lastname +'.txt'
            getcaptures()


    window.close()

