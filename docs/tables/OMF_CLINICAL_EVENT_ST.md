# OMF_CLINICAL_EVENT_ST

> omf_clinical_event_st

**Description:** Stores clinical events relating to encounter.  
**Table type:** ACTIVITY  
**Primary key:** `EVENT_ID`  
**Columns:** 43  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BODY_SITE_CD` | DOUBLE | NOT NULL |  | Body location where the collection was done (left arm, thumb, etc.) |
| 2 | `CATALOG_CD` | DOUBLE | NOT NULL |  | Foreign key to the order_catalog table. |
| 3 | `CE_RESULT_DT_NBR` | DOUBLE |  |  | The Cerner internal system date representation of the clinical event result. |
| 4 | `CE_RESULT_DT_TM` | DATETIME |  |  | The date/time clinical event result. |
| 5 | `CE_RESULT_MIN_NBR` | DOUBLE |  |  | The minute of day represented by the result. |
| 6 | `CE_RESULT_NBR_VALUE` | DOUBLE |  |  | The numeric result value. |
| 7 | `CE_RESULT_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 8 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 9 | `EVENT_CD` | DOUBLE | NOT NULL |  | Code_value associated with the clinical activity performed |
| 10 | `EVENT_ID` | DOUBLE | NOT NULL | PK | Unique identification number for a clinical event associated with the encounter |
| 11 | `EVENT_START_DT_NBR` | DOUBLE |  |  | The Julian date of the optional clinical date time for the start of the event. |
| 12 | `EVENT_START_DT_TM` | DATETIME |  |  | Optional clinical date time for the start of the event. |
| 13 | `EVENT_START_MIN_NBR` | DOUBLE |  |  | The minute of the day of the optional clinical date time for the start of the event. |
| 14 | `EVENT_START_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 15 | `EVENT_TITLE_TEXT` | VARCHAR(255) |  |  | The title for document results. |
| 16 | `NORMALCY_CD` | DOUBLE | NOT NULL |  | The code_value identifying the normalcy of the clinical result |
| 17 | `NORMAL_HIGH` | VARCHAR(20) |  |  | The upper limit of the normal range for the clinical result |
| 18 | `NORMAL_IND` | DOUBLE |  |  | Indicator identifying whether or not the clinical result was normal |
| 19 | `NORMAL_LOW` | VARCHAR(20) |  |  | The lower limit of the normal range for the clinical result |
| 20 | `ORDER_ID` | DOUBLE | NOT NULL |  | Unique foreign key to the orders table. |
| 21 | `PARENT_EVENT_ID` | DOUBLE | NOT NULL | FK→ | Provides a mechanism for logical grouping of events. I.e. supergroup and group tests. Same as EVENT_ID if current row is the highest level parent. |
| 22 | `PERFORM_PRSNL_ID` | DOUBLE | NOT NULL |  | Unique identification number for the person performing the clinical activity |
| 23 | `PERFORM_PRSNL_POSITION_CD` | DOUBLE | NOT NULL |  | The Cerner-defined position for the performing prsnl. |
| 24 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 25 | `PROCESS_FLAG` | DOUBLE |  |  | Flag used to determine how to process batched clinical event transactions. |
| 26 | `RESULT_UNITS_CD` | DOUBLE | NOT NULL |  | The units of the result. |
| 27 | `RESULT_VAL` | VARCHAR(255) |  |  | General Lab Clinical Event Results |
| 28 | `SERVICE_DATE` | VARCHAR(25) |  |  | The date that the clinical activity was performed |
| 29 | `SERVICE_DAY` | DOUBLE |  |  | The day of week that the clinical activity was performed |
| 30 | `SERVICE_DT_NBR` | DOUBLE |  |  | The Julian date on which the clinical event was performed |
| 31 | `SERVICE_DT_TM` | DATETIME |  |  | The date/time that the clinical activity was performed |
| 32 | `SERVICE_HOUR` | DOUBLE |  |  | The hour of the day that the clinical activity was performed |
| 33 | `SERVICE_MIN_NBR` | DOUBLE |  |  | The minute of the day on which the clinical event was performed |
| 34 | `SERVICE_MONTH` | DOUBLE |  |  | The month that the clinical activity was performed |
| 35 | `SERVICE_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 36 | `SOURCE_TYPE_CD` | DOUBLE | NOT NULL |  | Source of collection (blood, sputum, stool, etc.) |
| 37 | `SPECIMEN_ID` | DOUBLE | NOT NULL |  | Unique identifier for the specimen on the v500_specimen table |
| 38 | `TASK_ASSAY_CD` | DOUBLE | NOT NULL |  | Unique foreign key to the discrete_task_assay table. |
| 39 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 40 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 41 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 42 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 43 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `PARENT_EVENT_ID` | [OMF_CLINICAL_EVENT_ST](OMF_CLINICAL_EVENT_ST.md) | `EVENT_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [OMF_CLINICAL_EVENT_ST](OMF_CLINICAL_EVENT_ST.md) | `PARENT_EVENT_ID` |

