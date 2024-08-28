
import re
#import PySimpleGUI as sg
from pathlib import Path
import os
import glob

os.chdir('/home/michael/Desktop')

#os.chdir('smb://mmiesner@vm-dc2/Scanned Inbox/047-Michael-Miesner/eval backgrounds /')
#glob.glob('/smb://mmiesner@vm0dc2/ eval feedback * '  )
#os.getcwd()


sal = input("what is your salutation")
firstname = input("what is the patient's first name")
lastname = input("what is the patient's last name")
s_pro = input("he or she")
po_pro = input("his or her")
filename = input("What is the patient file name")


with open(filename, "r", encoding='utf-8') as f:
    data = f.read()
    # data = mmap.mmap(f.fileno(), 0)
    try:
        presenting = re.search(("(?<=Illness:)((.|\n)*)(?=Progress:)"), data)
    except AttributeError:
        presenting = re.search(("(?<=Illness:)((.|\n)*)(?=Treatment / Therapy)"), data)
    try:
        medical = re.search(("(?<=Health History:)((.|\n)*)(?=Psychiatric History and Treatment:)"), data)
    except AttributeError:
        medical = re.search(("(?<=Health History:)((.|\n)*)(?=Psychiatric History and Treatment:)"), data)
    try:
        meds = re.search(("(?<=Medications:)((.|\n)*)(?=Clinical Review Of Systems:)"), data)
    except AttributeError:
        meds = re.search(("(?<=Medications:)((.|\n)*)(?=Clinical Review Of Systems:)"), data)
    try:
        psyHx = re.search(("(?<=Psychiatric History and Treatment:)((.|\n)*)(?=Childhood History:)"), data)
    except AttributeError:
        psyHx = re.search(("(?<=Psychiatric History and Treatment:)((.|\n)*)(?=Childhood History:)"), data)
    try:
        education = re.search(("(?<=Childhood History:)((.|\n)*)(?=Safety Information:)"), data)
    except AttributeError:
        education = re.search(("(?<=Childhood History:)((.|\n)*)(?=Safety Information:)"), data)
    try:
        current_status = re.search(("(?<=Additional Personal Information:)((.|\n)*)(?=Family Dynamics:)"), data)
    except AttributeError:
        current_status = re.search(("(?<=Additional Personal Information:)((.|\n)*)(?=Family Dynamics:)"), data)
    try:
        Family = re.search(("(?<=Family Dynamics:)((.|\n)*)(?=Current Psychiatric Medications:)"), data)
    except AttributeError:
        Family = re.search(("(?<=Family Dynamics:)((.|\n)*)(?=Current Psychiatric Medications:)"), data)
    try:
        ROS = re.search(("(?<=Clinical Review Of Systems:)((.|\n)*)(?=Mental Status Examination:)"), data)
    except AttributeError:
        ROS = re.search(("(?<=Clinical Review Of Systems:)((.|\n)*)(?=Mental Status Examination:)"), data)
    #try:
     #   MSE = re.search(("(?<=Mental Status Examination:)((.|\n)*)(?=Risk Assessments:)"), data)
   # except AttributeError:
     #   MSE = re.search(("(?<=Mental Status Examination:)((.|\n)*)(?=Risk Assessments:)"), data)
    try:
        SA = re.search(("(?<=Drug and Alcohol History and Treatment:)((.|\n)*)(?=Additional Personal Information:)"), data)
    except AttributeError:
        SA = re.search(("(?<=Drug and Alcohol History and Treatment:)((.|\n)*)(?=Additional Personal Information:)"), data)
    try:
        SI = re.search(("(?<=Safety Information:)((.|\n)*)(?=Nutrition Information:)"), data)
    except AttributeError:
        SI = re.search(("(?<=Safety Information:)((.|\n)*)(?=Nutrition Information:)"), data)
    try:
        orientation = re.search(("(?<=Orientation:)((.|\n)*)(?=Appearance)"), data)
    except AttributeError:
        orientation = re.search(("(?<=Orientation:)((.|\n)*)(?=Appearance)"), data)
    try:
        affect = re.search(("(?<=Affect:)((.|\n)*)(?=Mood)"), data)
    except AttributeError:
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
    try:
        ADHDage = re.search(("(?<=Age Symptoms Noticed:)((.|\n)*)(?=Symptoms Present:)"), data)
    except AttributeError:
        ADHDage = re.search(("(?<=Age Symptoms Noticed:)((.|\n)*)(?=Symptoms Present:)"), data)
    try:
        SettingsPresent = re.search(("(?<=Symptoms Present:)((.|\n)*)(?=Interference:)"), data)
    except AttributeError:
        SettingsPresent = re.search(("(?<=Symptoms Present:)((.|\n)*)(?=Interference:)"), data)
    try:
        Interference = re.search(("(?<=Interference:)((.|\n)*)(?=Inattention :)"), data)
    except AttributeError:
        Interference = re.search(("(?<=Interference:)((.|\n)*)(?=Inattention :)"), data)
    try:
        Inattention = re.search(("(?<=Inattention :)((.|\n)*)(?=Impulsivity:)"), data)
    except AttributeError:
        Inattention = re.search(("(?<=Inattention :)((.|\n)*)(?=Impulsivity:)"), data)
    try:
        Impulsivity = re.search(("(?<=Impulsivity:)((.|\n)*)(?=Hyperactivity:)"), data)
    except AttributeError:
        Impulsivity = re.search(("(?<=Impulsivity:)((.|\n)*)(?=IHyperactivity:)"), data)
    try:
        Hyperactivity = re.search(("(?<=Hyperactivity:)((.|\n)*)(?=Consequences Experienced:)"), data)
    except AttributeError:
        Hyperactivity = re.search(("(?<=Hyperactivity:)((.|\n)*)(?=Consequences Experienced:)"), data)
    try:
        Consequences = re.search(("(?<=Consequences Experienced:)((.|\n)*)(?=Parental Insights:)"), data)
    except AttributeError:
        Consequences = re.search(("(?<=Consequences Experienced:)((.|\n)*)(?=Parental Insights:)"), data)
    try:
        Parents = re.search(("(?<=Parental Insights:)((.|\n)*)(?=Teacher Insights:)"), data)
    except AttributeError:
        Parents = re.search(("(?<=Parental Insights:)((.|\n)*)(?=Teacher Insights:)"), data)
    try:
        Teachers = re.search(("(?<=Teacher Insights:)((.|\n)*)(?=Mental Status Examination:)"), data)
    except AttributeError:
        Teachers = re.search(("(?<=Teacher Insights:)((.|\n)*)(?=Mental Status Examination:)"), data)
    try:
        DOI = re.search(r'((?<=Visit Date:)(\s+)(\d{2}/\d{2}/\d{4}))', data)
        print(DOI.group(0))
    except AttributeError:
        DOI = re.search(r'((?<=Visit Date:)(\s+)(\d{2}/\d{2}/\d{4}))', data)
        print(DOI.group(0))
with open('/home/michael/' +lastname + '.txt', 'w', encoding="utf-8") as f:

    if presenting:
        f.writelines(sal + " " + firstname + " " + lastname + " is a " + presenting.group(0))
    if medical:
        f.writelines("When discussing " + po_pro + " medical history," + s_pro + medical.group(0))
    if meds:
        f.writelines("When asked about " + po_pro + " current medications," + s_pro + " endorsed " + meds.group(0))
    if psyHx:
        f.writelines("When discussing " + po_pro + " psychiatric history," + psyHx.group(0))
    if education:
        f.writelines("When asked about " + po_pro + " educational history, " + s_pro + " endorsed" + education.group(0))
    if current_status:
        f.writelines("When asked about " + po_pro + " current living situation," + s_pro + " endorsed" + current_status.group(0))
    if Family:
        f.writelines("When discussing " + po_pro + " family background, " + s_pro + " indicated " + Family.group(0))

    f.writelines("\n")
    if ADHDage:
        f.writelines("During the clinical interview, time was spent discussing symptoms related to ADHD specifically." + firstname + " endorsed that these symptoms started around age" + ADHDage.group() + "")
    if SettingsPresent:
        f.writelines(s_pro + " noted that the symptoms exist in settings including" + SettingsPresent.group() +". ")
    if Interference:
        f.writelines("When discussing symptoms that are experienced, he endorsed that " + Interference.group() + "interferes with functioning." )
    if Inattention:
        f.writelines("When discussing symptoms that  " + s_pro + " experiences related to inattention," + s_pro + " endorsed" + Inattention.group() + ". ")
    if Impulsivity:
        f.writelines("When " + s_pro + " was asked about impulsivity, " + s_pro + " endorsed" + Impulsivity.group(0))
    if Hyperactivity:
        f.writelines("When " + s_pro + " was asked about hyperactivity, " + s_pro + " endorsed" + Hyperactivity.group(0))
    if Consequences:
        f.writelines("When " + s_pro + " was asked about consequences related to symptoms of ADHD, " + s_pro + " indicated " + Consequences.group(0))
    if Parents:
        f.writelines("When discussing " + po_pro + " parents' perspective on whether or not " + s_pro + " has ADHD,  " + s_pro + " endorsed" + Parents.group(0))
    if Teachers:
        f.writelines("When discussing " + po_pro + " former teachers' perspective on whether or not " + s_pro + " has ADHD,  " + s_pro + " endorsed"+ Teachers.group(0))
    f.writelines("\n")
    if ROS:
        f.writelines(ROS.group(0))
    if DOI:
        f.writelines("The noted date of interview was " + DOI)


    f.writelines("\n")
    #f.writelines(MSE.group(0))
    #f.writelines('\033[1;4m' + 'MENTAL STATUS EXAM' + '\033[0m')
    f.writelines("During the course of the clinical interview, time was spent performing a mental status examination. ")
    if orientation:
        f.writelines(sal + " " + firstname + " " + lastname + " was " + str(orientation.group()).strip() + " to person, place, time, and situation. ")
    if affect:
        f.writelines(s_pro.title() + " endorsed " + str(affect.group()).strip() + " affect. ")
    if mood:
        f.writelines(firstname + " endorsed " + po_pro + " mood as being " + str(mood.group()).strip().lower() + ". ")
    if attention and appearance:
        f.writelines("When discussing attention, " + s_pro + " endorsed it as being " + str(attention.group()).strip() + ". " + s_pro.title() + " appearance was observed to be " + str(appearance.group()).strip() + ".")
    if Reasoning:
        f.writelines(s_pro.title() + " endorsed reasoning that was " + str(Reasoning.group()).strip().lower() + ".")
    if nutrition:
        f.writelines(s_pro.title() + "When discussing nutrition, " + s_pro + "noted" + str(nutrition.group()).strip() + ". ")
    if Calcs and STM and LTM:
        f.writelines(s_pro.title() + " was able to perform " + str(Calcs.group()).strip() + " calculations such as word rotation and serial sevens. "+ s_pro.upper() +" rated " + po_pro + " short term memory as " + str(STM.group()).strip() + " and " + po_pro + " long term memory as " + str(LTM.group()).strip() + ". ")
    if ROT:
        f.writelines(s_pro.title() + " endorsed rate of thoughts as " + str(ROT.group()).strip().lower() + ". " )
    if FOK and Reasoning:
        f.writelines(s_pro.title() + " endorsed fund of knowledge as " + str(FOK.group()).strip() + " compared to " + po_pro + " peers. Language appeared " + str(Reasoning.group()).strip().lower() + ". ")
    if Judg and Insight:
        f.writelines(s_pro.title() + " rated judgment as being " + str(Judg.group()).strip() + " insight as " + str(Insight.group()).strip() + ". ")
    if Hallucinations and Delusions:
        f.writelines("When asked about hallucinations, " + s_pro + " stated there were" + str(Hallucinations.group()).strip() + ". Likewise " + s_pro + " endorsed delusions as " + str(Delusions.group()).strip() + ". ")
    if ThoughtContent and ThoughtProcessses:
        f.writelines("When discussing thought content, " + s_pro + " indicated " + str(ThoughtContent.group()).strip().lower() + ". When discussing thought processes, " + s_pro + " indicated " + str(ThoughtProcessses.group()).strip().lower() + ".")
    if SA:
        f.writelines("When discussing " + po_pro + " substance use background, " + s_pro + " indicated" + SA.group(0))
    if SI:
        f.writelines("When asked about " + po_pro + " suicidal or homicidal ideation " + s_pro + " indicated " + SI.group(0))

    # Read in the file
#with open('/home/michael/Desktop/' +lastname + '.txt', 'r') as file:
  #  filedata = file.read()

    # Replace the target string
 #   filedata = filedata.replace('Patient', s_pro.title())

    # Write the file out again
#with open('/home/michael/Desktop' +lastname + '.txt', 'w') as file:
 #       file.write(filedata)


print(" Done & Exiting")



