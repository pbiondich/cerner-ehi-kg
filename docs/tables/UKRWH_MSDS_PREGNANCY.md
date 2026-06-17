# UKRWH_MSDS_PREGNANCY

> Contains pregnancy details from NHS Maternity Services Data Set.

**Description:** UKRWH_MSDS_PREGNANCY  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 75

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ABNORMALITY_AT_DT_US_SCAN_IND` | VARCHAR(10) |  |  | An indication of whether any abnormalities were detected during a clinical investigation for a dating ultrasound scan. |
| 2 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 3 | `AGREED_EDD_METHOD_NHS` | VARCHAR(10) |  |  | The NHS code for the method used to calculate the Estimated Date of Delivery (Agreed). |
| 4 | `CARE_PRO_TYPE_NHS` | VARCHAR(10) |  |  | The NHS care professional type code of the first care professional seen by the mother within a maternity episode for antenatal care. |
| 5 | `CIG_PER_DAY_NBR` | DOUBLE |  |  | The number of cigarettes per day smoked by the mother, as identified at the Appointment Date (Formal Antenatal Booking). |
| 6 | `DEL_PLACE_CH_REASON_NHS` | VARCHAR(10) |  |  | The NHS code for delivery place change reason if the place of delivery is different from the place originally intended, either in the type of place or geographically. |
| 7 | `DT_US_SCAN_OFER_STATUS_NHS` | VARCHAR(10) |  |  | The NHS code for dating ultrasound scan offer status. |
| 8 | `EOP_SMOKING_STATUS_NHS` | VARCHAR(10) |  |  | The NHS code for smoking status of the mother, reported by the mother after the delivery of the baby. |
| 9 | `EPISIOTOMY_REASON_NHS` | VARCHAR(10) |  |  | The NHS code for episiotomy performed reason during Labour and Delivery. |
| 10 | `ETHNIC_CAT_MOTHER_NHS` | VARCHAR(10) |  |  | The NHS ethnic category code for the mother in a maternity episode. |
| 11 | `EXTRACT_DT_TM` | DATETIME |  |  | Date and Time of when extract was created. |
| 12 | `FETUS_PRE_ONSET_LAB_NHS` | VARCHAR(10) |  |  | The NHS code for presentation of the Fetus. |
| 13 | `FIRST_LANG_ENG_FLG` | VARCHAR(10) |  |  | An indication of whether a persons first language is English. N - First language is not English, Y - First language is English. |
| 14 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | First date/time row was inserted into table. |
| 15 | `FOLIC_ACID_SUPP_STATUS_NHS` | VARCHAR(10) |  |  | The NHS status code of whether a woman has been taking or intends to take folic acid supplements. |
| 16 | `GEST_AGE_AT_DT_US_SCAN` | VARCHAR(40) |  |  | The gestation length of a fetus episode recorded as the total number of days measured at the dating ultrasound scan. |
| 17 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Unique number assigned by Health Facts. Typically the universal Cerner assigned client id of the health system. |
| 18 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL |  | Unique number assigned by Health Facts. Typically the universal Cerner assigned client id of the sending health system but may be adjusted if there is >1 HF feed from the client. |
| 19 | `HEIGHT_AT_BOOKING` | VARCHAR(10) |  |  | the height of the mother measured during an antenatal period. The unit of measurement is metres (m). |
| 20 | `INTED_DEL_PLACE_TYPE_NHS` | VARCHAR(10) |  |  | The NHS delivery place type code where the pregnant woman plans to have her baby. The first intended delivery place type is recorded, as designated by the care professional in consultation with the patient. |
| 21 | `INTED_DEL_SITE_CODE_NACS` | VARCHAR(10) |  |  | The Organisation Site Code of the organisation that is the intended place of delivery of the baby as part of a maternity episode. |
| 22 | `INTED_DEL_WARD_TYPE_NHS` | VARCHAR(10) |  |  | The NHS code of midwife unit or ward type that is intended as the place of delivery for the current midwife episode. |
| 23 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | Last date/time row was updated. |
| 24 | `LEAD_CARE_PRO_TYPE_NHS` | VARCHAR(10) |  |  | The NHS code of care professional type identified in the care plan with overall responsibility for care of the mother during the maternity episode. |
| 25 | `LOCAL_PATIENT_IDENT` | VARCHAR(40) |  |  | The Local Patient Identifier of the mother in a maternity episode. |
| 26 | `LOC_AGREED_EDD_DT_TM` | DATETIME |  |  | The clinically agreed estimated date of delivery converted to local datetime. |
| 27 | `LOC_C_SECTION_PROC_DT_TM` | DATETIME |  |  | The procedure date and time when the Caesarean Section took place during labour and delivery converted to local datetime. |
| 28 | `LOC_DECEASED_DT_TM` | DATETIME |  |  | Person death date and time for the mother in a maternity episode converted to local datetime. |
| 29 | `LOC_DECISION_TO_DELIVER_DT_TM` | DATETIME |  |  | The start date and time of the decision to deliver converted to local datetime. |
| 30 | `LOC_DELIVERY_HPS_ST_DT_TM` | DATETIME |  |  | The start date and time for a mother during a maternity episode as part of the onset of labour, or for a caesarean section procedure converted to local datetime. |
| 31 | `LOC_DISCH_POST_DEL_HPS_DT_TM` | DATETIME |  |  | The date and time that a Patient is discharged from hospital, following readmission in the Postpartum period converted to local datetime. |
| 32 | `LOC_DT_SCAN_ACT_OFFER_DT_TM` | DATETIME |  |  | An activity offer date for dating scan converted to local datetime. |
| 33 | `LOC_DT_US_SCAN_PROC_DT_TM` | DATETIME |  |  | An activity date for the Clinical Investigation of dating ultrasound scan converted to local datetime. |
| 34 | `LOC_FIRST_ANTE_APP_DT_TM` | DATETIME |  |  | The date converted to local datetime on which the pregnant woman was assessed and arrangements made for antenatal care as part of the Pregnancy Episode. This is not necessarily the occasion on which arrangements were made for delivery. |
| 35 | `LOC_LABOUR_ONSET_DT_TM` | DATETIME |  |  | The start date and time for Established Labour Onset converted to local datetime. |
| 36 | `LOC_LAST_MENSTRUAL_DT_TM` | DATETIME |  |  | The date of the first day of the last menstrual period for a female person converted to local datetime. |
| 37 | `LOC_MAT_CARE_PLAN_DT_TM` | DATETIME |  |  | The date on which a care plan was agreed with the patient for a maternity episode converted to local datetime. |
| 38 | `LOC_MAT_DISCHARGE_DT_TM` | DATETIME |  |  | The date on which the mother ceased to be cared for in a maternity episode converted to local datetime. This will be the last contact date with a midwife when care is then continued by a specialist community public health nurse, health visitor. |
| 39 | `LOC_MOTHER_DOB_DT_TM` | DATETIME |  |  | Date of birth of the mother in a maternity episode converted to local datetime. |
| 40 | `LOC_PREG_FIRST_CONTACT_DT_TM` | DATETIME |  |  | The date at which a pregnant woman first contacted the NHS to access antenatal care converted to local datetime. |
| 41 | `LOC_ROM_DT_TM` | DATETIME |  |  | The start date and time of the rupture of membranes during labour and delivery converted to local datetime. |
| 42 | `LOC_SECOND_LAB_ONSET_ST_DT_TM` | DATETIME |  |  | The start date and time for second stage of labour onset converted to local datetime. |
| 43 | `LOC_THIRD_LAB_ONSET_END_DT_TM` | DATETIME |  |  | The end date and time for third stage of labour end converted to local datetime. |
| 44 | `MAT_CARE_PLAN_TYPE_NHS` | VARCHAR(10) |  |  | The NHS code of care plan type for a maternity episode. |
| 45 | `MOTHER_COMPLEX_SOC_FCT_IND` | VARCHAR(10) |  |  | An indication of whether the mother in a maternity episode is deemed to be subject to complex social factors, as defined by the National Institute for Health and Care Excellence guidance. |
| 46 | `MOTHER_EMP_STATUS_NHS` | VARCHAR(10) |  |  | Employment status of the mother at the Appointment Date (Formal Antenatal Booking). |
| 47 | `MOTHER_MH_PREDICT_DETECT_IND` | VARCHAR(10) |  |  | An indication of whether the recommended questions for prediction and detection of mental health issues have been asked of the mother at the Appointment Date (Formal Antenatal Booking). |
| 48 | `MOTHER_SUPPORT_STATUS_FLG` | VARCHAR(10) |  |  | An indication of whether the mother reports feeling she is supported in pregnancy and looking after the baby, from partner, family or friends. N - Does not feel supported, Y - Feels supported. Z - Person asked but declined to respond. |
| 49 | `NHS_NBR_IDENT` | VARCHAR(40) |  |  | The NHS Number of the mother in a maternity episode. |
| 50 | `NHS_NBR_STATUS_NHS` | VARCHAR(10) |  |  | The NHS status indicator code of the NHS Number (Mother). |
| 51 | `NO_FETUSES_DT_US_SCAN_NBR` | DOUBLE |  |  | The number of fetuses counted within a particular pregnancy episode noted at the dating ultrasound scan. |
| 52 | `PARTNER_EMP_STATUS_NHS` | VARCHAR(10) |  |  | Employment status of the partner of the mother at the Appointment Date (Formal Antenatal Booking). |
| 53 | `PCT_MRN_NACS` | VARCHAR(10) |  |  | The Organisation Code of the Organisation that assigned the Local Patient Identifier (Mother). |
| 54 | `PCT_RESIDENCE_NACS` | VARCHAR(10) |  |  | The Organisation Code derived from the patients postcode of usual address. |
| 55 | `PHYSICAL_DISABILITY_FLG` | VARCHAR(10) |  |  | An indication of whether a person has a physical disability. This does not include learning disabilities. N - Does not have disability, Y - Has disablity. |
| 56 | `PLACENTA_DELIV_METHOD_NHS` | VARCHAR(10) |  |  | The NHS code for method by which a placenta was removed at the end of Labour and Delivery. |
| 57 | `PNATAL_LEAD_PRVD_NACS` | VARCHAR(10) |  |  | The Organisation Code of the postnatal lead provider Organisation for the purpose of the Maternity Services Data Set. |
| 58 | `POSTCODE` | VARCHAR(10) |  |  | The Postcode of the address nominated by the patient (Mother). |
| 59 | `PREGNANCY_SK` | VARCHAR(40) |  |  | Millennium system generated unique identifier for a pregnancy. |
| 60 | `PREV_C_SECTIONS_NBR` | DOUBLE |  |  | The number of previous caesarean sections performed. |
| 61 | `PREV_TOT_LIVE_BIRTHS_NBR` | DOUBLE |  |  | The number of registrable live births by the mother. |
| 62 | `PREV_TOT_LOSSES_24WKS_NBR` | DOUBLE |  |  | The recorded number of terminations and previous losses before 24 weeks of pregnancy (i.e. less than 23 weeks and 6 days) for a woman. |
| 63 | `PREV_TOT_STILL_BIRTHS_NBR` | DOUBLE |  |  | The number of registrable still births by the mother i.e. a birth after a gestation of 24 weeks (168 days), or more, where a baby shows no identifiable signs of life at delivery. |
| 64 | `ROM_METHOD_NHS` | VARCHAR(10) |  |  | The NHS code for method by which membranes were ruptured during labour and delivery. |
| 65 | `ROM_REASON_NHS` | VARCHAR(10) |  |  | The NHS reason code of why an Artificial Rupture of Membranes (ARM) was performed during labour and delivery. |
| 66 | `SMOKING_STATUS_NHS` | VARCHAR(10) |  |  | The NHS code for smoking status of the mother during a maternity episode, reported by the mother at the Appointment Date (Formal Antenatal Booking). |
| 67 | `SUBSTANCE_USE_STATUS_NHS` | VARCHAR(10) |  |  | The NHS code for substance misused status reported by the mother, for a substance misused other than alcohol or tobacco, at the Appointment Date (Formal Antenatal Booking). |
| 68 | `TOTAL_UPDATES` | DOUBLE |  |  | The numbers of updates that have occurred on this table. |
| 69 | `UKRWH_MSDS_PREG_KEY` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the UKRWH_MSDS_PREGNANCY table. |
| 70 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 71 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. |
| 72 | `UPDT_TASK` | VARCHAR(40) |  |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 73 | `UPDT_USER` | VARCHAR(40) |  |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 74 | `WEEKLY_ALCOHOL_UNITS_NBR` | DOUBLE |  |  | The number of alcohol units per week consumed by the mother as identified at the Appointment Date (Formal Antenatal Booking). |
| 75 | `WEIGHT_AT_BOOKING` | VARCHAR(10) |  |  | The weight of the mother measured during an antenatal period. The unit of measurement is kilograms (kg). |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

