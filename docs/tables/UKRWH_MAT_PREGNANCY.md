# UKRWH_MAT_PREGNANCY

> Contains pregnancy details assocaited to a maternity encounter

**Description:** UKRWH_MAT_PREGNANCY  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 105

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCOMMODATION_NM_SK` | VARCHAR(100) |  |  | Current Accommodation Type (Mother at Booking) Millennium Nomenclature Identifier |
| 2 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 3 | `ALCOHOL_USE_NBR` | DOUBLE |  |  | The typical number of units of alcohol the mother drinks - per week - as reported at the Booking Appointment |
| 4 | `BLOOD_PATCH_IND` | DOUBLE |  |  | Blood Patch Procedure performed Indicator. 1 indicates a Blood Patch procedure was recorded - 0 that no procedure was recorded. |
| 5 | `BMI_BOOKING` | DOUBLE |  |  | Body Mass Index at Booking |
| 6 | `CHOOSING_TERMINTION_PREG_NM_SK` | VARCHAR(100) |  |  | Haemaglobinopathy Plan of Care |
| 7 | `DEATH_LAB_WD_DT_TM` | DATETIME |  |  | Date/time of death of mother |
| 8 | `DEL_LOC_CHG_REASON_PREG_NM_SK` | VARCHAR(100) |  |  | Planned place of birth change reason |
| 9 | `DOWNS_SERUM_SCREEN_NM_SK` | VARCHAR(100) |  |  | Whether or not screening for Downs Syndrome was offered - accepted or declined |
| 10 | `ECV_SCT_IND` | DOUBLE |  |  | An Indicator of whether the woman has had a procedure external cephalic version based on Procedures recorded. 1 indicates a procedure has occurred - 0 that none has been recorded. |
| 11 | `EDUCATION_NM_SK` | VARCHAR(100) |  |  | Latest education level at booking |
| 12 | `EMPLOY_STATUS_NM_SK` | VARCHAR(100) |  |  | Whether or not the mother is in employment - as identified at the Booking Appointment |
| 13 | `EPISIOTOMY_NM_SK` | VARCHAR(40) |  |  | Indication for episiotomy |
| 14 | `EXTRACT_DT_TM` | DATETIME |  |  | Date/time of extraction execution time |
| 15 | `FAMILY_ORIGIN_MOTHER_NM_SK` | VARCHAR(100) |  |  | The ethnicity of the mother in a maternity episode as specified by herself |
| 16 | `FAMILY_ORIGIN_PARTNER_NM_SK` | VARCHAR(100) |  |  | The ethnicity of the babies father in a maternity episode |
| 17 | `FINAL_EDD_DT_TM` | DATETIME |  |  | The Estimated Date of Delivery - as agreed by ultrasound scan - LMP or Clinical Assessment. |
| 18 | `FIRST_ANTE_ASSESS_DT_TM` | DATETIME |  |  | Referred to as the Booking Appointment - the date on which the pregnant woman was assessed and arrangements made for antenatal care as part of the Pregnancy Episode. This is not necessarily the occasion on which arrangements were made for delivery. |
| 19 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | First date/time row was inserted into table. |
| 20 | `FULL_DIL_DT_TM` | DATETIME |  |  | Date/time when established labour is confirmed - regular painful contractions and progressive cervical dilatation from 4 cm |
| 21 | `GEST_AGE_PREG_END` | VARCHAR(40) |  |  | Gestation at DATE TIME OF BIRTH (BABY) in in weeks and days - in the format #Weeks#Days . |
| 22 | `GEST_AGE_PREG_START` | VARCHAR(40) |  |  | Gestation date at the time of the open pregnancy start date. In weeks and days - in the format #Weeks#Days . This will be earliest Estimate for the Pregnancy. |
| 23 | `GEST_DEATH_CONF_DT_TM` | DATETIME |  |  | The date associated to the entry of Fetal Death being associated to a Pregnancy in the Diagnosis and Problems Control. |
| 24 | `GRAVIDA_NBR` | DOUBLE |  |  | Count of all past pregnancies including the current one in context |
| 25 | `HAEMAGLOBINOPATHY_SCREEN_NM_SK` | VARCHAR(100) |  |  | Whether or not a mother was offered a haemoglobinopathy serum screening test - and the subsequent response to the offer |
| 26 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Unique number assigned by Health Facts. Typically the universal Cerner assigned client id of the health system. |
| 27 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL |  | Unique number assigned by Health Facts. Typically the universal Cerner assigned client id of the sending health system but may be adjusted if there is >1 HF feed from the client. |
| 28 | `HEIGHT_BOOKING_CM` | DOUBLE |  |  | The height of a person on a given date. The unit of measurement is metres. |
| 29 | `HEPB_ANTIGEN_SCREEN_NM_SK` | VARCHAR(100) |  |  | Whether or not a mother was offered a screening test and whether or not she declined or accepted. |
| 30 | `HIV_SCREEN_NM_SK` | VARCHAR(100) |  |  | Whether or not a mother was offered a screening test and whether or not she declined or accepted. |
| 31 | `HX_EPIDURAL_NBR` | DOUBLE |  |  | The Number of previous labours with a anesthesia type of Epidural |
| 32 | `HX_PREG_CS_EL_NBR` | DOUBLE |  |  | The Number of previous pregnancies with outcomes of C-Section Elective |
| 33 | `HX_PREG_CS_EM_AFT_FAIL_IN_NBR` | DOUBLE |  |  | The Number of previous pregnancies with outcomes of C-Section EM after failed induction |
| 34 | `HX_PREG_CS_EM_NBR` | DOUBLE |  |  | The Number of previous pregnancies with outcomes of C-Section Emergency |
| 35 | `HX_PREG_ECTOPIC_MED_NBR` | DOUBLE |  |  | The number of previous pregnancies with outcomes of Ectopic pregnancy Medical Management |
| 36 | `HX_PREG_ECTOPIC_NBR` | DOUBLE |  |  | The Number of previous pregnancies with outcomes of Ectopic . |
| 37 | `HX_PREG_ECTOPIC_SURG_NBR` | DOUBLE |  |  | The Number of previous pregnancies with outcomes of Ectopic pregnancy laporotomy |
| 38 | `HX_PREG_SPONT_ABORT_DC_NBR` | DOUBLE |  |  | The Number of previous pregnancies with outcomes of Spontaneous Abortion with D&C . |
| 39 | `HX_PREG_SPONT_ABORT_NBR` | DOUBLE |  |  | The number of previous pregnancies with outcomes of Spontaneous abortion . |
| 40 | `HX_PREG_SPONT_NBR` | DOUBLE |  |  | The Number of previous pregnancies with outcomes of Spontaneous Vertex OR Vaginal Breech spontaneous prior to current pregnancy in context. |
| 41 | `HX_PREG_THERAP_ABORT_MED_NBR` | DOUBLE |  |  | The Number of previous pregnancies with outcomes of Therapeutic Abortion - Medical . |
| 42 | `HX_PREG_THERAP_ABORT_SURG_NBR` | DOUBLE |  |  | The Number of previous pregnancies with outcomes of Therapeutic Abortion - Surgical . |
| 43 | `HX_PREG_VAG_BREECH_NBR` | DOUBLE |  |  | The Number of previous pregnancies with outcomes of Vaginal Breech spontaneous OR Vaginal Breech Assisted |
| 44 | `HX_PREG_VAG_DESTRUCTION_NBR` | DOUBLE |  |  | The Number of previous pregnancies with outcomes of Vaginal Other including destruction . |
| 45 | `HX_PREG_VAG_FORCEP_NBR` | DOUBLE |  |  | The Number of previous pregnancies with outcomes of Vaginal Forcep Assist |
| 46 | `HX_PREG_VAG_SPONT_NBR` | DOUBLE |  |  | The Number of previous pregnancies with outcomes of Vaginal Spontaneous . |
| 47 | `HX_PREG_VAG_VACCUM_NBR` | DOUBLE |  |  | The Number of previous pregnancies with outcomes of Vaginal Vacuum Assist |
| 48 | `HX_PREG_VBAC_NBR` | DOUBLE |  |  | The Number of previous pregnancies with outcomes of Vaginal Birth after Caesarean . |
| 49 | `KNOWN_SOC_SERV_NM_SK` | VARCHAR(100) |  |  | Does the woman have a social worker at time of booking - Yes or No. |
| 50 | `LAB_AUGMENTATION_NM_SK` | VARCHAR(100) |  |  | Augmentation of labour |
| 51 | `LAB_ONSET_DT_TM` | DATETIME |  |  | Date/time when established labour is confirmed - regular painful contractions and progressive cervical dilatation from 4 cm |
| 52 | `LAB_ONSET_METHOD_NM_SK` | VARCHAR(100) |  |  | Method of onset of labour |
| 53 | `LAB_STAGE1_TOTAL` | DOUBLE |  |  | Length of Stage I of Labour in minutes |
| 54 | `LAB_STAGE2_TOTAL` | DOUBLE |  |  | Length of Stage II of Labour in minutes |
| 55 | `LAB_STAGE3_TOTAL` | DOUBLE |  |  | Length of Stage III of Labour in minutes |
| 56 | `LAB_SUPPORT_NM_SK` | VARCHAR(100) |  |  | Support during labour |
| 57 | `LAB_TOTAL` | DOUBLE |  |  | Total length of labour in minutes |
| 58 | `LAST_METHOD_CONTRACEPT_NM_SK` | VARCHAR(100) |  |  | Last method of contraception (Mother at Booking) Millennium Nomenclature Identifier |
| 59 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | Last date/time row was updated. |
| 60 | `LOCAL_PATIENT_IDENT` | VARCHAR(40) |  |  | The Local Patient Identifier of the mother in a maternity episode. |
| 61 | `LOC_DEATH_LAB_WD_DT_TM` | DATETIME |  |  | Date/time of death of mother converted to local datetime |
| 62 | `LOC_FINAL_EDD_DT_TM` | DATETIME |  |  | The Estimated Date of Delivery - as agreed by ultrasound scan - LMP or Clinical Assessment converted to local datetime. |
| 63 | `LOC_FIRST_ANTE_ASSESS_DT_TM` | DATETIME |  |  | Referred to as the Booking Appointment - the date on which the pregnant woman was assessed and arrangements made for antenatal care as part of the Pregnancy Episode. This is not necessarily the occasion on which arrangements were made for delivery converted to local datetime. |
| 64 | `LOC_FULL_DIL_DT_TM` | DATETIME |  |  | Date/time when established labour is confirmed - regular painful contractions and progressive cervical dilatation from 4 cm converted to local datetime |
| 65 | `LOC_MOTHER_DOB_DT_TM` | DATETIME |  |  | Date of birth of the mother in a maternity episode converted to local datetime |
| 66 | `MIDWIFE_TEAM_NAME` | VARCHAR(255) |  |  | The name of the trust defined midwifery team the woman is assigned to where applicable. |
| 67 | `MOTHER_DOB_DT_TM` | DATETIME |  |  | Date of birth of the mother in a maternity episode |
| 68 | `MOTHER_NAME` | VARCHAR(255) |  |  | The Full Name of the mother in a maternity episode. |
| 69 | `NHS_NBR_IDENT` | VARCHAR(40) |  |  | The NHS Number of the mother in a maternity episode. |
| 70 | `OCCUP_MOTHER` | VARCHAR(255) |  |  | Woman s occupation at booking as Text. |
| 71 | `OCCUP_PARTNER` | VARCHAR(255) |  |  | Husband/Partner s Occupation at booking as Text. |
| 72 | `PARA_NBR` | DOUBLE |  |  | The number live births from previous pregnancies |
| 73 | `PARTNER_PAID_EMP_BKING_NM_SK` | VARCHAR(100) |  |  | Whether or not the partner (who may or may not be the father) is employed - as identified at the Booking Appointment. |
| 74 | `PARTNER_REC_SUB_USE_NM_SK` | VARCHAR(100) |  |  | Partner Substance Use Status (Mother at Booking) Millennium Nomenclature Identifier |
| 75 | `PERSON_SK` | VARCHAR(40) |  |  | The Millennium system generated unique person identifier of the mother in a maternity episode. |
| 76 | `PLACENTA_APPEARANCE_NM_SK` | VARCHAR(100) |  |  | Appearance of placenta |
| 77 | `PLACENTA_MAN_REMOVAL_IND` | DOUBLE |  |  | An indicator of whether a Manual Removal of retained Placenta procedure was carried out. 1 indicates a procedure was recorded - 0 that none was recorded. |
| 78 | `PLANNED_DEL_LOC_LAB_NM_SK` | VARCHAR(100) |  |  | Planned place of birth change reason |
| 79 | `PLANNED_DEL_LOC_PREG_NM_SK` | VARCHAR(100) |  |  | Intended place of delivery |
| 80 | `PLANNED_IOL_IND` | DOUBLE |  |  | Planned induction Indicator. 1 indicates that an order was placed to indicate that an Induction was planned - 0 indicates there was no record of such an order. |
| 81 | `PLANNED_LSCS_IND` | DOUBLE |  |  | Planned Caesarean Indicator. 1 indicates that an order was placed to indicate that an Caesarean was planned - 0 indicates there was no record of such an order. |
| 82 | `PREGNANCY_SK` | VARCHAR(40) |  |  | Millennium system generated unique identifier for a pregnancy. |
| 83 | `PREG_TYPE_SCT_VALUE` | VARCHAR(100) |  |  | Type of pregnancy e.g. singleton - twins - triples etc. |
| 84 | `PRES_FETUS_VE_NM_SK` | VARCHAR(100) |  |  | The presentation of the (first) fetus at onset of labour |
| 85 | `PREV_PREG_PROBLEM_IND` | DOUBLE |  |  | An indicator of whether the mother has a history of any complications listed for any previous pregnancy outcomes . 1 indicating a complication being present for a previous pregnancy - 0 representing no complications associated to previous pregnancy being present. |
| 86 | `REC_SUB_USE_NM_NM_SK` | VARCHAR(100) |  |  | The mother s self-reported status of whether or not she has used or is using non medicinal drugs or other substances at the booking appointment |
| 87 | `ROM_DT_TM` | DATETIME |  |  | Date/time on which membranes ruptured |
| 88 | `ROM_METHOD_NM_SK` | VARCHAR(100) |  |  | The way in which membranes were ruptured |
| 89 | `RUBELLA_IGG_SCREEN_NM_SK` | VARCHAR(100) |  |  | Whether or not a mother was offered a screening test and whether or not she declined or accepted. |
| 90 | `SMOKE_BOOKING_NM_SK` | VARCHAR(100) |  |  | The mother s self-reported smoking status at the Booking Appointment |
| 91 | `SMOKE_LIVES_WITH_NM_SK` | VARCHAR(100) |  |  | Living with anyone who smokes |
| 92 | `SMOKING_STATUS_DEL_NM_SK` | VARCHAR(100) |  |  | The mother s self-reported smoking status - specifically after the birth of the baby (synonym with at delivery ). |
| 93 | `SUPPORT_STATUS_NM_SK` | VARCHAR(100) |  |  | Whether or not the mother feels she is supported in pregnancy and looking after a baby - from partner - family or friends - as identified at the Booking Appointment |
| 94 | `SYPHILIS_SCREEN_NM_SK` | VARCHAR(100) |  |  | Offer status of syphilis screening |
| 95 | `TOBAC_USE_NBR` | DOUBLE |  |  | The number of cigarettes smoked per day - by the mother - as identified at the booking appointment (where they are a current smoker) |
| 96 | `TOTAL_BLOOD_LOSS` | DOUBLE |  |  | Total Blood Loss recorded associated to the Delivery in Millilitres |
| 97 | `TOTAL_UPDATES` | DOUBLE |  |  | The numbers of updates that have occurred on this table. |
| 98 | `UKRWH_MAT_PREGNANCY_KEY` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the UKRWH_MAT_PREGNANCY table. |
| 99 | `UNBOOKED_NM_SK` | VARCHAR(100) |  |  | Booking Status at last Telephone Contact |
| 100 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 101 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. |
| 102 | `UPDT_TASK` | VARCHAR(40) |  |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 103 | `UPDT_USER` | VARCHAR(100) |  |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 104 | `WEIGHT_BOOKING_KG` | DOUBLE |  |  | Identifies the measured weight of a person on a given date. The type of measurement is Kilograms. |
| 105 | `WEIGHT_EST_KG` | DOUBLE |  |  | Identifies the estimated weight of a person on a given date. The type of measurement is Kilograms. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

