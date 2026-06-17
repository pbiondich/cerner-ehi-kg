# OMF_ABSTRACT_DATA_ST

> Stores abstract data relating to an encounter. Currently supports ProFile's abstract data.

**Description:** Stores abstract data relating to an encounter.  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 20

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ABSTRACT_DATA_ID` | DOUBLE | NOT NULL |  | The unique identification number for the value of an abstract data element. |
| 2 | `ABSTRACT_DEF_CD` | DOUBLE | NOT NULL |  | The unique identifier for an abstract data element. |
| 3 | `ABSTRACT_FIELD_TYPE_CD` | DOUBLE | NOT NULL |  | Defines the data type of the abstract data element. |
| 4 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `BEG_EFFECTIVE_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 7 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 8 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 9 | `END_EFFECTIVE_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 10 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 16 | `VALUE_CD` | DOUBLE | NOT NULL |  | The code value that corresponds to the abstract data element (if the data type is codeset). Since it is abstract data, it can come from any code set. |
| 17 | `VALUE_DT_TM` | DATETIME |  |  | The date/time that corresponds to the abstract data element (if the data type is DATE). |
| 18 | `VALUE_FREE_TEXT` | VARCHAR(255) |  |  | The character string that corresponds to the abstract data element (if the data type is free text). |
| 19 | `VALUE_NUMBER` | DOUBLE |  |  | The number that corresponds to the abstract data element (if the data type is number or Boolean). |
| 20 | `VALUE_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

