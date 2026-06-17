# CODING_HIST

> Used to store history of the coding information.

**Description:** Coding History  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 30

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ASCPAY` | DOUBLE |  |  | This is the ascpay field |
| 3 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 4 | `BIRTH_WEIGHT` | DOUBLE |  |  | This is the birth weight from the coding system. |
| 5 | `CANCER_CODE_CNT` | DOUBLE | NOT NULL |  | The number of diagnoses that have the Cancer Notification form needed. |
| 6 | `CODING_DT_TM` | DATETIME |  |  | Date and time coding of episode took place. |
| 7 | `CODING_ENTITY_ID` | DOUBLE |  | FK→ | Foreign key, Unique generated number that identifies a single row on the CODING_ENTITY table. |
| 8 | `CODING_HIST_ID` | DOUBLE | NOT NULL |  | The unique primary key of this table. It is an internally assigned number. |
| 9 | `CODING_PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Primary key ID from the parent Coding or Coding_Specialty table. |
| 10 | `CODING_PARENT_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | Parent Coding or Coding_Specialty table name. |
| 11 | `CODING_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Personnel who last coded the episode. |
| 12 | `COMPLETED_DT_TM` | DATETIME |  |  | This is the date and time that the coding record was saved as completed. |
| 13 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 14 | `CREATE_DT_TM` | DATETIME |  |  | The date and time the row was created. |
| 15 | `CREATE_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The personnel id of the user that created the row, from the personnel table (prsnl). This is the value of the unique primary identifier of the personnel table. It is an internal system assigned number |
| 16 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 17 | `ENCNTR_SLICE_ID` | DOUBLE | NOT NULL | FK→ | Identifies an Encounter as it relates to a time slice. |
| 18 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 19 | `EVENT_ID` | DOUBLE | NOT NULL |  | This is the value of a unique secondary identifier of the clinical_event table. It is an internal system assigned number. |
| 20 | `LENGTH_OF_STAY` | DOUBLE |  |  | This is the Length of stay from the coding system |
| 21 | `MERGED_ENCNTR_ID` | DOUBLE | NOT NULL |  | The encounter ID for the encounter that has been merged with this one. (If it is a merged account). |
| 22 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Primary key ID from the parent table. |
| 23 | `PARENT_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | Parent table name. |
| 24 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 25 | `SVC_CAT_HIST_ID` | DOUBLE | NOT NULL | FK→ | This field is a unique identifier for the service category history table. |
| 26 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 27 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 28 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 29 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 30 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CODING_ENTITY_ID` | [CODING_ENTITY](CODING_ENTITY.md) | `CODING_ENTITY_ID` |
| `CODING_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `CREATE_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `ENCNTR_SLICE_ID` | [ENCNTR_SLICE](ENCNTR_SLICE.md) | `ENCNTR_SLICE_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `SVC_CAT_HIST_ID` | [SERVICE_CATEGORY_HIST](SERVICE_CATEGORY_HIST.md) | `SVC_CAT_HIST_ID` |

