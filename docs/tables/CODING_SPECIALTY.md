# CODING_SPECIALTY

> Stores coding information, including length of stay, birthweight and ascpay for speciality coding instances.

**Description:** Coding Specialty  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 31

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ASCPAY` | DOUBLE |  |  | This is the ascpay field |
| 6 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 7 | `BIRTH_WEIGHT` | DOUBLE |  |  | This is the birth weight from the coding system |
| 8 | `CANCER_CODE_CNT` | DOUBLE | NOT NULL |  | the number of diagnoses that have the Cancer Notification form needed |
| 9 | `CODING_DT_TM` | DATETIME |  |  | Date and time coding of episode took place |
| 10 | `CODING_ENTITY_ID` | DOUBLE |  | FK→ | Foreign key, Unique generated number that identifies a single row on the CODING_ENTITY table. |
| 11 | `CODING_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the coding_specialty table. |
| 12 | `CODING_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Personnel who last coded this episode. |
| 13 | `COMPLETED_DT_TM` | DATETIME |  |  | Thi si the date and time the coding specialty record was saved as completed. |
| 14 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 15 | `CREATE_DT_TM` | DATETIME |  |  | The date and time the row was created |
| 16 | `CREATE_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The personnel id of the user that created the row, from the personnel table (prsnl). This is the value of the unique primary identifier of the personnel table. It is an internal system assigned number. |
| 17 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 18 | `ENCNTR_SLICE_ID` | DOUBLE | NOT NULL | FK→ | Identifies an encounter as it relates to a time slice. |
| 19 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 20 | `EVENT_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the clinical_event table. It is an internal system assigned number. |
| 21 | `LENGTH_OF_STAY` | DOUBLE |  |  | This is the Length of stay from the coding system |
| 22 | `MERGED_ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | The encounter ID for the encounter that has beeen merged with this one. (If it is a merged account). |
| 23 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Primary key ID from the parent table. |
| 24 | `PARENT_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | Parent table name. |
| 25 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 26 | `SVC_CAT_HIST_ID` | DOUBLE | NOT NULL | FK→ | This field is a unique identifier for the service category history table. |
| 27 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 28 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 29 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 30 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 31 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CODING_ENTITY_ID` | [CODING_ENTITY](CODING_ENTITY.md) | `CODING_ENTITY_ID` |
| `CODING_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `CREATE_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `ENCNTR_SLICE_ID` | [ENCNTR_SLICE](ENCNTR_SLICE.md) | `ENCNTR_SLICE_ID` |
| `MERGED_ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `SVC_CAT_HIST_ID` | [SERVICE_CATEGORY_HIST](SERVICE_CATEGORY_HIST.md) | `SVC_CAT_HIST_ID` |

