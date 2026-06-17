# MIC_STAT_ORDER

> This summary table is comprised of Microbiology order level information, which is used in the Microbiology Statistical Reporting package.

**Description:** Microbiology Statistical Order  
**Table type:** ACTIVITY  
**Primary key:** `ORDER_ID`  
**Columns:** 51  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCESSION_NBR` | VARCHAR(20) |  |  | This field uniquely identifies an order or a group of orders. |
| 2 | `BODY_SITE_CD` | DOUBLE | NOT NULL |  | This field contains the internal identification code identifying the body site from which this specimen was drawn. |
| 3 | `CATALOG_CD` | DOUBLE | NOT NULL |  | This field contains the internal identification code of the orderable procedure. This could be used to join to the ORDER_CATALOG table. |
| 4 | `CATALOG_SEQ` | DOUBLE | NOT NULL |  | This field is used in conjunction with the MIC_STAT_ORDER.CATALOG_CD field in order to ensure uniqueness within an accession. For example, if an accession contained to C Wound orders then this field would be valued with '1' for the first C Wound and '2' for the second C Wound. |
| 5 | `COLLECT_DT_NBR` | DOUBLE | NOT NULL |  | The date number when the orderable procedure was collected. Used to gather date information from the OMF_DATE table. |
| 6 | `COLLECT_DT_TM` | DATETIME |  |  | This field contains the date and time at which the orderable procedure was collected. |
| 7 | `COLLECT_LOC_BUILDING_CD` | DOUBLE | NOT NULL |  | This field contains the internal identification code for the building location at which this order was collected. This could be used to join to the LOCATION table. |
| 8 | `COLLECT_LOC_FACILITY_CD` | DOUBLE | NOT NULL |  | This field contains the internal identification code for the facility location at which this order was collected. This could be used to join to the LOCATION table. |
| 9 | `COLLECT_LOC_NURSE_UNIT_CD` | DOUBLE | NOT NULL |  | This field contains the internal identification code for the nurse unit location at which this order was collected. This could be used to join to the LOCATION table. |
| 10 | `COLLECT_MIN_NBR` | DOUBLE | NOT NULL |  | The minute number when the orderable procedure was collected. Used to get time information from the OMF_TIME table. |
| 11 | `COLLECT_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | This field contains the internal identification code for the person whom collected the order. This could be used to join to the PRSNL table. |
| 12 | `COMPLETE_DT_NBR` | DOUBLE | NOT NULL |  | The date number when the orderable procedure was completed. Used to gather date information from the OMF_DATE table. |
| 13 | `COMPLETE_DT_TM` | DATETIME |  |  | This field contains the date and time at which the orderable procedure was completed. |
| 14 | `COMPLETE_MIN_NBR` | DOUBLE | NOT NULL |  | The minute number when the orderable procedure was completed. Used to get time information from the OMF_TIME table. |
| 15 | `COMPLETE_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | This field contains the internal identification code for the person whom completed the order. This could be used to join to the PRSNL table. |
| 16 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 17 | `DAYS_TO_POSITIVE` | DOUBLE | NOT NULL |  | This field contains the number of days from which a culture was started to when it was identified as positive. |
| 18 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 19 | `EXT_ACCESSION_NBR` | VARCHAR(30) |  |  | This field contains the accession number value from a foreign system. This field is only populated for records uploaded from a foreign system. |
| 20 | `FREETEXT_SOURCE_ID` | DOUBLE | NOT NULL | FK→ | This field contains the internal identification code to the LONG_TEXT row, which contains a textual value for free textsource associated with this orderable procedure. |
| 21 | `INTERP_TEXT_ID` | DOUBLE | NOT NULL | FK→ | This field contains the internal identification code to the LONG_TEXT row, which contains a textual value for interpretive data associated with this orderable procedure. |
| 22 | `NOSOCOMIAL_IND` | DOUBLE | NOT NULL |  | This field indicates whether an infection was acquired during a hospital stay. Valid values include: 0 = No nosocomial infection 1 = Nosocomial infection |
| 23 | `ORDER_COMMENT_ID` | DOUBLE | NOT NULL | FK→ | This field contains the internal identification code to the LONG_TEXT row, which contains a textual value for order comment associated with this orderable procedure. |
| 24 | `ORDER_DT_NBR` | DOUBLE | NOT NULL |  | The date number when the orderable procedure was ordered. Used to gather date information from the OMF_DATE table. |
| 25 | `ORDER_DT_TM` | DATETIME |  |  | This field contains the date and time at which the orderable procedure was ordered. |
| 26 | `ORDER_ID` | DOUBLE | NOT NULL | PK FK→ | This field contains the unique value assigned to each orderable procedure associated with an order. For example: if there are two procedures on the same accession number, then each procedure will have a unique order id. |
| 27 | `ORDER_LOC_BUILDING_CD` | DOUBLE | NOT NULL |  | This field contains the internal identification code for the building location at which this order was placed. This could be used to join to the LOCATION table. |
| 28 | `ORDER_LOC_FACILITY_CD` | DOUBLE | NOT NULL |  | This field contains the internal identification code for the facility location at which this order was placed. This could be used to join to the LOCATION table. |
| 29 | `ORDER_LOC_NURSE_UNIT_CD` | DOUBLE | NOT NULL |  | This field contains the internal identification code for the nurse unit location at which this order was placed. This could be used to join to the LOCATION table. |
| 30 | `ORDER_MIN_NBR` | DOUBLE | NOT NULL |  | The minute number when the orderable procedure was ordered. Used to get time information from the OMF_TIME table. |
| 31 | `ORDER_NOTE_ID` | DOUBLE | NOT NULL | FK→ | This field contains the internal identification code to the LONG_TEXT row, which contains a textual value for order note associated with this orderable procedure. |
| 32 | `ORDER_PROVIDER_FT` | VARCHAR(100) |  |  | This field contains the name of a free text ordering provider. This column is ONLY populated from a historical upload. |
| 33 | `ORDER_PROVIDER_ID` | DOUBLE | NOT NULL | FK→ | This field contains the internal identification code for the ordering provider. This could be used to join to the PRSNL table. |
| 34 | `ORDER_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | This field contains the internal identification code for the person whom placed the order. This could be used to join to the PRSNL table. |
| 35 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 36 | `POSITIVE_IND` | DOUBLE |  |  | This field indicates whether or not the procedure is considered positive. Microbiology procedures are considered positive when a preliminary or final report is issued that includes a positive response or organism. Valid values include: 0 = Not positive 1 = Positive |
| 37 | `PURGE_DT_TM` | DATETIME |  |  | This field contains the date at which this order will be eligible to purge. |
| 38 | `RECEIVE_DT_NBR` | DOUBLE | NOT NULL |  | The date number when the orderable procedure was received. Used to gather date information from the OMF_DATE table. |
| 39 | `RECEIVE_DT_TM` | DATETIME |  |  | This field contains the date and time at which the orderable procedure was received. |
| 40 | `RECEIVE_MIN_NBR` | DOUBLE | NOT NULL |  | The minute number when the orderable procedure was received. Used to get time information from the OMF_TIME table. |
| 41 | `RECEIVE_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | This field contains the internal identification code for the person whom received the order. This could be used to join to the PRSNL table. |
| 42 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL |  | This field contains the internal identification code for the service resource at which this order was performed. This could be used to join to the SERVICE_RESOURCE table. |
| 43 | `SOURCE_CD` | DOUBLE | NOT NULL |  | This field contains the internal identification code of the source to which this specimen was drawn. |
| 44 | `START_DT_NBR` | DOUBLE | NOT NULL |  | The date number when the orderable procedure was started. Used to gather date information from the OMF_DATE table. |
| 45 | `START_DT_TM` | DATETIME |  |  | This field identifies the start date and time of the orderable procedure. |
| 46 | `START_MIN_NBR` | DOUBLE | NOT NULL |  | The minute number when the orderable procedure was started. Used to get time information from the OMF_TIME table. |
| 47 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 48 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 49 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 50 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 51 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `COLLECT_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `COMPLETE_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `FREETEXT_SOURCE_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `INTERP_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `ORDER_COMMENT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `ORDER_NOTE_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `ORDER_PROVIDER_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `ORDER_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `RECEIVE_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (3)

| From table | Column |
|------------|--------|
| [MIC_STAT_MEDICATION](MIC_STAT_MEDICATION.md) | `ORDER_ID` |
| [MIC_STAT_PATHOGEN](MIC_STAT_PATHOGEN.md) | `ORDER_ID` |
| [MIC_STAT_TASK](MIC_STAT_TASK.md) | `ORDER_ID` |

