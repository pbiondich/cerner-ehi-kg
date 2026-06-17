# UKRWH_CDS_APC_DELIVERY

> Contains CDS Delivery details at the level of a Brith relating to an Admitted Patient Care CDS Event.

**Description:** UK Reporting Warehouse Commissioning Data Delivery  
**Table type:** ACTIVITY  
**Primary key:** `UKRWH_CDS_APC_DELIVERY_KEY`  
**Columns:** 44  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVITY_LOCATION_TYPE_NHS` | VARCHAR(3) |  |  | The type of LOCATION for an ACTIVITY |
| 2 | `ANAESTHETIC_DURING_LABOUR_NHS` | VARCHAR(1) |  |  | ANAESTHETIC GIVEN DURING LABOUR OR DELIVERY is derived from attribute ANAESTHETIC OR ANALGESIC CATEGORY and PERIOD ADMINISTERED which records whether anaesthetic was given during labour/delivery, and the type used |
| 3 | `ANAESTHETIC_POST_LABOUR_NHS` | VARCHAR(1) |  |  | ANAESTHETIC GIVEN POST LABOUR OR DELIVERY is derived from attribute ANAESTHETIC OR ANALGESIC CATEGORY and PERIOD ADMINISTERED which records whether anaesthetic was given after delivery, and the type used. |
| 4 | `ANTENATAL_GMP_IDENT` | VARCHAR(8) |  |  | This is the GENERAL MEDICAL PRACTITIONER PPD CODE for the GENERAL MEDICAL PRACTITIONER responsible for the PATIENT's antenatal care |
| 5 | `ANTENATAL_GP_PRACTICE_ORG_NACS` | VARCHAR(12) |  |  | This is the ORGANISATION CODE for the General Medical Practitioner Practice responsible for the PATIENT's antenatal care |
| 6 | `CDS_BATCH_CONTENT_SK` | VARCHAR(40) | NOT NULL |  | Unique identifier for each cds item. This is the unique CDS ID reported to the NHS. |
| 7 | `DELIVERY_DT_TM` | DATETIME |  |  | This records the date & time of delivery for each registrable birth and corresponds to the attribute PERSON BIRTH DATE. |
| 8 | `DELIVERY_LOC_CHANGE_REASON_NHS` | VARCHAR(1) |  |  | If the place of delivery is different from the place originally intended, either in the type of place or geographically, the reasons for change should be classified as below |
| 9 | `FIRST_ANTENATAL_ASSMNT_DT_TM` | DATETIME |  |  | The date on which the pregnant woman was assessed and arrangements made for antenatal care as part of the Pregnancy Episode. This is not necessarily the occasion on which arrangements were made for delivery. |
| 10 | `FIRST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | Date and time of the first process |
| 11 | `GESTATION_LABOUR_ONSET_WEEKS` | DOUBLE |  |  | This is the same as attribute GESTATION LENGTH. This records a period of between 10 to 49 weeks in completed weeks of the gestation length at the onset of labour within a CDS message. |
| 12 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Unique number assigned by Health Facts. Typically the universal Cerner assigned client id of the health system. |
| 13 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL |  | Unique number assigned by Health Facts. Typically the universal Cerner assigned client id of the sending health system but may be adjusted if there is >1 HF feed from the client. |
| 14 | `INTND_DELIVERY_LOC_TYPE_NHS` | VARCHAR(1) |  |  | This is the delivery place type where the pregnant woman plans to have her baby. The first intended delivery place type is recorded, as designated by the caring professional in consultation with the client. |
| 15 | `LABOUR_DLVRY_ONSET_METHD_NHS` | VARCHAR(1) |  |  | The method by which the process of labour began, or delivery by caesarean section occurred. |
| 16 | `LAST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | Date and time of the second process |
| 17 | `LOCATION_CLASS_NHS` | VARCHAR(2) |  |  | A classification for use within CDS messages of the physical location within which the recorded patient event occurs |
| 18 | `MOTHER_ADDRESS_FORMAT_NHS` | VARCHAR(2) |  |  | A code to determine the format of the associated PATIENT USUAL ADDRESS (MOTHER) data within CDS Birth Episode and CDS Home Birth |
| 19 | `MOTHER_BIRTH_DT_TM` | DATETIME |  |  | The birth date & time for the mother |
| 20 | `MOTHER_LINE1_ADDR` | VARCHAR(35) |  |  | The first text string comprising one line of an ADDRESS (of Mother). |
| 21 | `MOTHER_LINE2_ADDR` | VARCHAR(35) |  |  | The second text string comprising one line of an ADDRESS.(of Mother) |
| 22 | `MOTHER_LINE3_ADDR` | VARCHAR(35) |  |  | The third text string comprising one line of an ADDRESS.(of Mother) |
| 23 | `MOTHER_LINE4_ADDR` | VARCHAR(35) |  |  | The fourth text string comprising one line of an ADDRESS.(of Mother) |
| 24 | `MOTHER_LINE5_ADDR` | VARCHAR(35) |  |  | The fifth text string comprising one line of an ADDRESS.(of Mother) |
| 25 | `MOTHER_LOCAL_PATIENT_IDENT` | VARCHAR(10) |  |  | This uniquely identifies the mother within CDS Birth Episode and CDS Home Birth where the baby's identity is recorded by use of LOCAL PATIENT IDEN |
| 26 | `MOTHER_LOCAL_PATIENT_ORG_NACS` | VARCHAR(12) |  |  | This is the ORGANISATION CODE of the ORGANISATION that assigned the LOCAL PATIENT IDENTIFIER (MOTHER). |
| 27 | `MOTHER_NHS_NBR_IDENT` | VARCHAR(10) |  |  | The NHS Number of the mother within CDS Birth Episode and CDS Home Birth where the baby is recorded by use of NHS NUMBER. |
| 28 | `MOTHER_NHS_NBR_STATUS_NHS` | VARCHAR(2) |  |  | The NHS Number Status Indicator of the NHS NUMBER (MOTHER) within CDS Birth Episode and CDS Home Birth. The values to be used are as for NHS NUMBER STATUS INDICATOR. |
| 29 | `MOTHER_OVERSEAS_VS_NHS` | VARCHAR(1) |  |  | The status of a MOTHER who is an Overseas Visitor |
| 30 | `MOTHER_PATIENT_UNSTRUCT_ADDR` | VARCHAR(175) |  |  | Mother's full unstructured address |
| 31 | `MOTHER_PCT_RESIDENCE_ORG_NACS` | VARCHAR(12) |  |  | PCT OF RESIDENCE is the same as the attribute ORGANISATION CODE (retired 1 Sep 2008) |
| 32 | `MOTHER_POSTCODE` | VARCHAR(25) |  |  | The code allocated by the Post Office to identify a group of postal delivery points |
| 33 | `MOTHER_WITHHELD_FLG` | VARCHAR(1) |  |  | Indicates whether mother's data has been anonymised |
| 34 | `MOTHER_WITHHLD_IDENT_REASN_NHS` | VARCHAR(2) |  |  | NHS values which identifys that the mother's record has been purposely anonymised for a valid reason |
| 35 | `NBR_OF_BABIES_TOT` | DOUBLE |  |  | This derived data item records the number of REGISTERABLE BIRTHS (live or still born at a particular delivery). |
| 36 | `NBR_PREVIOUS_PREGNANCIES_TOT` | DOUBLE |  |  | The number of previous pregnancies resulting in one or more REGISTERABLE BIRTHS |
| 37 | `TOTAL_UPDATES` | DOUBLE | NOT NULL |  | The numbers of updates that have occurred on this table. |
| 38 | `UKRWH_CDS_APC_DELIVERY_KEY` | DOUBLE | NOT NULL | PK | This is a unique local ACTIVITY IDENTIFIER used to identify a delivery during the encounter |
| 39 | `UKRWH_CDS_APC_EPISODE_KEY` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the ukrwh cds apc episode table. It is an internal system assigned number. |
| 40 | `UPDATE_USER` | VARCHAR(40) | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table |
| 41 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 42 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 43 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 44 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `UKRWH_CDS_APC_EPISODE_KEY` | [UKRWH_CDS_APC_EPISODE](UKRWH_CDS_APC_EPISODE.md) | `UKRWH_CDS_APC_EPISODE_KEY` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [UKRWH_CDS_APC_BIRTH](UKRWH_CDS_APC_BIRTH.md) | `UKRWH_CDS_APC_DELIVERY_KEY` |

