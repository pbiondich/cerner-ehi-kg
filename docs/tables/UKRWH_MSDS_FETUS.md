# UKRWH_MSDS_FETUS

> Contains fetus and birth details from NHS Maternity Services Data Set.

**Description:** UKRWH_MSDS_FETUS  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 40

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACT_DEL_PLACE_TYPE_NHS` | VARCHAR(10) |  |  | The NHS code for the actual place type of delivery. |
| 3 | `ACT_DEL_SITE_CODE_NACS` | VARCHAR(10) |  |  | The Organisation Site Code of the Organisation where the baby was delivered as part of a Maternity Episode. |
| 4 | `ACT_DEL_WARD_TYPE_NHS` | VARCHAR(10) |  |  | The NHS code of midwife unit or ward type of the actual place of delivery for the registrable birth. |
| 5 | `APGAR_SCORE_AT_5MIN` | VARCHAR(10) |  |  | The Apgar score at five minutes after birth. The Apgar Score is determined by evaluating the newborn baby on five criteria (Appearance, Pulse, Grimace, Activity and Respiration) on a scale from zero to two, then summing up the values obtained. The resulting Apgar Score ranges from zero to ten. |
| 6 | `BABY_PHENOT_SEX_NHS` | VARCHAR(10) |  |  | The NHS code for classification of person (Baby) phenotypic sex. |
| 7 | `BIRTH_ORDER_NBR` | DOUBLE |  |  | The sequence in which the baby was born, with 1 indicating the first or only birth in the sequence (i.e. singleton), 2 indicating the second birth in the sequence, 3 indicating the third, etc. |
| 8 | `BIRTH_WEIGHT` | VARCHAR(10) |  |  | The birth weight where the unit of measurement is grams (g). |
| 9 | `DEL_IN_WATER_IND` | VARCHAR(10) |  |  | An indication of whether the registrable birth was delivered in a birthing pool. |
| 10 | `DEL_METHOD_NHS` | VARCHAR(10) |  |  | The NHS delivery method code for the current baby. |
| 11 | `DIS_BFEEDING_STATUS_NHS` | VARCHAR(10) |  |  | The breastfeeding status recorded at the discharge date time (mother post delivery hospital provider spell). |
| 12 | `EXTRACT_DT_TM` | DATETIME |  |  | Date and Time of when extract was created. |
| 13 | `FETUS_ORDER_NBR` | DOUBLE |  |  | The outcome of a fetus episode for the current maternity episode. |
| 14 | `FIRST_FEED_BM_STATUS_NHS` | VARCHAR(10) |  |  | The type of breast milk a baby receives for a Baby First Feed. |
| 15 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the first ETL process started that created this record. |
| 16 | `GEST_AGE_AT_BIRTH` | VARCHAR(40) |  |  | Gestation length in days at the person birth date of the registrable birth. |
| 17 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Unique number assigned by Health Facts. Typically the universal Cerner assigned client id of the health system. |
| 18 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL |  | Unique number assigned by Health Facts. Typically the universal Cerner assigned client id of the sending health system but may be adjusted if there is >1 HF feed from the client. |
| 19 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the last ETL process started that updated this record. |
| 20 | `LOCAL_PATIENT_IDENT` | VARCHAR(40) |  |  | The Local Patient Identifier of the baby. |
| 21 | `LOCAL_PATIENT_IDENT_MUM` | VARCHAR(40) |  |  | The Local Patient Identifier of the mother in a maternity episode. |
| 22 | `LOC_BABY_BIRTH_DT_TM` | DATETIME |  |  | Date and time of birth of the baby converted to local datetime. |
| 23 | `LOC_BABY_DEATH_DT_TM` | DATETIME |  |  | Person death date and time converted to local datetime for a baby (registrable birth), if the child died within 28 days after the Person Birth Date (Baby). |
| 24 | `LOC_FIRST_ANTE_APP_DT_TM` | DATETIME |  |  | The date converted to local datetime on which the pregnant woman was assessed and arrangements made for antenatal care as part of the Pregnancy Episode. This is not necessarily the occasion on which arrangements were made for delivery. |
| 25 | `LOC_FIRST_FEED_DT_TM` | DATETIME |  |  | The start date and time of a baby first feed converted to local datetime. |
| 26 | `LOC_PREG_OUTCOME_DT_TM` | DATETIME |  |  | Date and Time of the pregnancy outcome for the current Fetus. |
| 27 | `NHS_NBR_IDENT` | VARCHAR(40) |  |  | The NHS Number of the baby. |
| 28 | `NHS_NBR_STATUS_NHS` | VARCHAR(10) |  |  | The NHS status indicator code of the NHS Number (Baby). |
| 29 | `PCT_MRN_NACS` | VARCHAR(10) |  |  | The Organisation Code of the Organisation that assigned the Local Patient Identifier (Baby). |
| 30 | `PREGNANCY_FETUS_SK` | VARCHAR(40) |  |  | Millennium Pregnancy Identifier with fetus order number to link fetus with registrable birth. |
| 31 | `PREGNANCY_SK` | VARCHAR(40) |  |  | Millennium system generated unique identifier for a pregnancy. |
| 32 | `PREG_FETUS_OUTCOME_NHS` | VARCHAR(10) |  |  | The NHS code for pregnancy outcome of a fetus episode for the current maternity episode. |
| 33 | `SKIN_TO_SKIN_1HR_IND` | VARCHAR(10) |  |  | An indication of whether skin to skin contact was made between mother and baby within one hour of delivery of the baby, following Labour and Delivery. |
| 34 | `TOTAL_UPDATES` | DOUBLE |  |  | The numbers of updates that have occurred on this table. |
| 35 | `UKRWH_MSDS_FETUS_KEY` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the UKRWH_MSDS_FETUS table. |
| 36 | `UKRWH_MSDS_PREG_KEY` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the UKRWH_MSDS_PREGNANCY table. |
| 37 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 38 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 39 | `UPDT_TASK` | VARCHAR(40) |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 40 | `UPDT_USER` | VARCHAR(40) |  |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

