# BB_SPEC_EXPIRE_OVRD

> This table records when the user overrides (shortens or extends) the default specimen expiration date and time or when the system overrides the specimen expiration using a flex parameter.

**Description:** Blood Bank Specimen Expiration Override  
**Table type:** ACTIVITY  
**Primary key:** `BB_SPEC_EXPIRE_OVRD_ID`  
**Columns:** 18  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BB_SPEC_EXPIRE_OVRD_ID` | DOUBLE | NOT NULL | PK | Uniquely identifies a row created when the user overrides (shorten or extends) the default specimen expiration date and time or when the system overrides the specimen expiration using a flex parameter. |
| 6 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 7 | `EXCEPTION_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the corresponding row on the BB_EXCEPTION table. |
| 8 | `NEW_SPEC_EXPIRE_DT_TM` | DATETIME |  |  | The date and time a specimen has expired and a new specimen is required for a person. |
| 9 | `OVERRIDE_DT_TM` | DATETIME | NOT NULL |  | Date and Time the override occurred either by system override or user override. |
| 10 | `OVERRIDE_REASON_CD` | DOUBLE | NOT NULL |  | Reason the specimen expiration was overridden. |
| 11 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | Person related to this specimen expiration override. |
| 12 | `PREV_SPEC_EXPIRE_DT_TM` | DATETIME |  |  | The date and time associated with the specimen before the override. This may have been based on the default or flex expiration or the date from a previous override. |
| 13 | `SPECIMEN_ID` | DOUBLE | NOT NULL | FK→ | Contains the identifier related to this specimen override record. |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `EXCEPTION_ID` | [BB_EXCEPTION](BB_EXCEPTION.md) | `EXCEPTION_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `SPECIMEN_ID` | [V500_SPECIMEN](V500_SPECIMEN.md) | `SPECIMEN_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [BB_SPEC_EXP_OVRD_PROD](BB_SPEC_EXP_OVRD_PROD.md) | `BB_SPEC_EXPIRE_OVRD_ID` |

