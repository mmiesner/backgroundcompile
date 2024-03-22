
import re
#import PySimpleGUI as sg
from pathlib import Path
import os

os.chdir('/home/michael/Desktop/')

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
        presenting = re.search(("(?<=Illness:)((.|\n)*)(?=Treatment / Therapy)"), data)
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
        Family = re.search(("(?<=Additional Personal Information:)((.|\n)*)(?=Family Dynamics:)"), data)
    except AttributeError:
        Family = re.search(("(?<=Additional Personal Information:)((.|\n)*)(?=Family Dynamics:)"), data)
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


with open('/home/michael/Google Drive/current evals/' +lastname + '.txt', 'w', encoding="utf-8") as f:

    if presenting:
        f.writelines(sal + " " + firstname + " " + lastname + " is a " + presenting.group(0))
    if medical:
        f.writelines("When discussing " + po_pro + " medical history," + s_pro + medical.group(0))
    if meds:
        f.writelines("When asked about " + po_pro + " current medications," + s_pro + "endorsed" + meds.group(0))
    if psyHx:
        f.writelines("When discussing " + po_pro + " psychiatric history," + psyHx.group(0))
    if education:
        f.writelines("When asked about " + po_pro + " educational history," + s_pro + "endorsed" + education.group(0))
    if current_status:
        f.writelines("When asked about " + po_pro + " current living situation," + s_pro + "endorsed" + current_status.group(0))
    if Family:
        f.writelines("When discussing " + po_pro + " family background, " + s_pro + " indicated " + Family.group(0))
    if ROS:
        f.writelines(ROS.group(0))
    f.writelines("\n")
    #f.writelines(MSE.group(0))
    f.writelines('\033[1;4m' + 'MENTAL STATUS EXAM' + '\033[0m')
    f.writelines("During the course of the clinical interview, time was spent performing a mental status examination. ")
    if orientation:
        f.writelines(sal + " " + firstname + " " + lastname + " was " + str(orientation.group()).strip() + " to person, place, time, and situation. ")
    if affect:
        f.writelines(s_pro.title() + " endorsed " + str(affect.group()).strip() + " affect. ")
    if mood:
        f.writelines(firstname + " endorsed " + po_pro + " mood as being " + str(mood.group()).strip() + ". ")
    if attention and appearance:
        f.writelines("When discussing attention, " + s_pro + " endorsed it as being " + str(attention.group()).strip() + " and appearance and " + str(appearance.group()).strip() + ".")
    if ROT and Reasoning:
        f.writelines(s_pro.title() + " endorsed " + str(ROT.group()).strip() + "appearance and " + str(Reasoning.group()).strip() + ".")
    if nutrition:
        f.writelines(s_pro.title() + "When discussing nutrition, " + s_pro + "noted" + str(nutrition.group()).strip() + ".")
    if Calcs and STM and LTM:
        f.writelines(s_pro.title() + " was able to perform " + str(Calcs.group()).strip() + "calculations such as word rotation and serial sevens."+ s_pro +"rated " + po_pro + " short term memory as " + str(STM.group()).strip() + " and " + po_pro + " long term memory as " + str(LTM.group()).strip() + ".")
    if ROT:
        f.writelines(s_pro.title() + " endorsed rate of thoughts as " + str(ROT.group()).strip() + ". " )
    if FOK and Reasoning:
        f.writelines(s_pro.title() + " endorsed fund of knowledge as " + str(FOK.group()).strip() + " compared to his peers. Language appeared " + str(Reasoning.group()).strip() + ". ")
    if Judg and Insight:
        f.writelines(s_pro.title() + " rated judgement as being " + str(Judg.group()).strip() + " insight as " + str(Insight.group()).strip() + ".")
    if Hallucinations and Delusions:
        f.writelines("When asked about hallucinations, " + po_pro + " stated " + str(Hallucinations.group()).strip() + ". Likewise " + s_pro + " endorsed delusions as" + str(Delusions.group()).strip() + ".")
    if ThoughtContent and ThoughtProcessses:
        f.writelines("When discussing thought content, " + po_pro + "indicated" + str(ThoughtContent.group()).strip() + ". When discussing  thought processes, " + s_pro + " indicated " + str(ThoughtProcessses.group()).strip() + ".")
    if SA:
        f.writelines("When discussing " + po_pro + " substance use background," + s_pro + "indicated" + SA.group(0))
    if SI:
        f.writelines("When asked about " + po_pro + " suicidal or homicidal ideation " + s_pro + " indicated " + SI.group(0))

    print(" Done & Exiting")



