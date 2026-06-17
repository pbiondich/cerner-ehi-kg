# UKRWH_CDS_APC_BIRTH

> Contains CDS Birth details at the level of a Brith relating to an Admitted Patient Care CDS Event.

**Description:** UK Reporting Warehouse Commissioning Data Set Birth  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 34

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVITY_LOCATION_TYPE_NHS` | VARCHAR(3) |  |  | The type of LOCATION for an ACTIVITY |
| 3 | `ACT_DELIVERY_PLACE_TYPE_NHS` | VARCHAR(1) |  |  | This is the actual place type of delivery |
| 4 | `BABY_BIRTH_DT_TM` | DATETIME |  |  | The date & time on which a baby was born or is officially deemed to have been born. |
| 5 | `BABY_BIRTH_WEIGHT_GRAMS_TOT` | DOUBLE |  |  | The baby's weight in grams between 0001 to 9998 grams. |
| 6 | `BABY_LOCAL_PATIENT_IDENT` | VARCHAR(10) |  |  | This uniquely identifies the baby within CDS Delivery Episode and CDS Home Delivery where the mother's identity is recorded by use of LOCAL PATIENT IDENTIFIER. |
| 7 | `BABY_LOCAL_PATIENT_ORG_NACS` | VARCHAR(12) |  |  | This is the ORGANISATION CODE of the ORGANISATION that assigned the LOCAL PATIENT IDENTIFIER (BABY). |
| 8 | `BABY_NHS_NBR_IDENT` | VARCHAR(10) |  |  | The NHS Number of the baby within CDS Delivery Episode and CDS Home Delivery where the mother is recorded by use of NHS NUMBER. |
| 9 | `BABY_NHS_NBR_STATUS_NHS` | VARCHAR(2) |  |  | The NHS Number Status Indicator of the NHS NUMBER (BABY) within CDS Delivery Episode and CDS Home Delivery. |
| 10 | `BABY_OVERSEAS_VS_NHS` | VARCHAR(1) |  |  | The status of a BABY who is an Overseas Visitor |
| 11 | `BABY_SEX_CD_NHS` | VARCHAR(1) |  |  | The gender code of the baby at birth |
| 12 | `BABY_WITHHELD_FLG` | VARCHAR(1) |  |  | Indicates whether baby's data has been anonymised |
| 13 | `BABY_WITHHELD_IDENT_REASON_NHS` | VARCHAR(2) |  |  | NHS values which identifys that the baby's record has been purposely anonymised for a valid reason |
| 14 | `BIRTH_ORDER_NBR` | DOUBLE |  |  | The sequence in which the baby was born, if part of a delivery having multiple births |
| 15 | `CDS_BATCH_CONTENT_SK` | VARCHAR(40) | NOT NULL |  | Unique identifier for each cds item. This is the unique CDS ID reported to the NHS. |
| 16 | `DELIVERY_LOC_IDENT` | VARCHAR(1) |  |  | A coded classification for place of delivery |
| 17 | `DELIVERY_METHOD_NHS` | VARCHAR(1) |  |  | The method by which a woman is delivered of a baby which is a REGISTERABLE BIRTH. |
| 18 | `DELIVERY_PRSNL_STATUS_NHS` | VARCHAR(1) |  |  | This is normally the status of the individual who delivers the baby. When the delivery is carried out by a student, the individual supervising the delivery should be the one recorded as conducting it. This may be different for each birth in a multiple birth. |
| 19 | `FIRST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | Date and time of the first process |
| 20 | `GESTATION_ASSESSMENT_NBR_WEEKS` | DOUBLE |  |  | This is the same as attribute GESTATION LENGTH and records a period of between 10 to 49 weeks in completed weeks that is a clinical assessment of gestation length within a CDS message. |
| 21 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Unique number assigned by Health Facts. Typically the universal Cerner assigned client id of the health system. |
| 22 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL |  | Unique number assigned by Health Facts. Typically the universal Cerner assigned client id of the sending health system but may be adjusted if there is >1 HF feed from the client. |
| 23 | `LAST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | Date and time of the second process |
| 24 | `LIVE_STILL_BIRTH_IND_NHS` | VARCHAR(1) |  |  | An indicator of whether the birth was a live or still birth. A still birth is a birth after a gestation of 24 weeks (168 days) where the baby shows no identifiable signs of life at delivery |
| 25 | `LOCATION_CLASS_NHS` | VARCHAR(2) |  |  | A classification for use within CDS messages of the physical location within which the recorded patient event occurs |
| 26 | `RESUSCITATION_METHOD_NHS` | VARCHAR(1) |  |  | It records the means by which regular respiration of the baby was attempted. This is not recorded for stillbirths. |
| 27 | `TOTAL_UPDATES` | DOUBLE | NOT NULL |  | The numbers of updates that have occurred on this table. |
| 28 | `UKRWH_CDS_APC_BIRTH_KEY` | DOUBLE | NOT NULL |  | This is a unique local ACTIVITY IDENTIFIER used to identify a birth in augmented care period. |
| 29 | `UKRWH_CDS_APC_DELIVERY_KEY` | DOUBLE | NOT NULL | FK→ | This is a unique local ACTIVITY IDENTIFIER used to identify a delivery in augmented care period. |
| 30 | `UPDATE_USER` | VARCHAR(40) | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table |
| 31 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 32 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 33 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 34 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `UKRWH_CDS_APC_DELIVERY_KEY` | [UKRWH_CDS_APC_DELIVERY](UKRWH_CDS_APC_DELIVERY.md) | `UKRWH_CDS_APC_DELIVERY_KEY` |

