# ABST_CODING_RELTN

> Relationship between code and abstracting field

**Description:** ABSTRACTING CODING RELATION  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 19

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ABSTRACT_FIELD_DEF_CD` | DOUBLE | NOT NULL |  | this is the unique identifier to the abstract field def table |
| 2 | `ABST_CODING_RELTN_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the abst_coding_reltn table. It is an internal system assigned number. It is filled out if the media was moved from another media. |
| 3 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 4 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 5 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 6 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 7 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 8 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 9 | `ENCNTR_SLICE_ID` | DOUBLE | NOT NULL | FK→ | Identifies an Encounter as it relates to a time slice. |
| 10 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 11 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the parent table. It is an internal system assigned number. It is filled out if the media was moved from another media. |
| 12 | `PARENT_ENTITY_NAME` | VARCHAR(255) |  |  | This is the name of the parent table |
| 13 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 14 | `SVC_CAT_HIST_ID` | DOUBLE | NOT NULL | FK→ | This is the unique identifier for the service category history table. |
| 15 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 16 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 17 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 18 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 19 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `ENCNTR_SLICE_ID` | [ENCNTR_SLICE](ENCNTR_SLICE.md) | `ENCNTR_SLICE_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `SVC_CAT_HIST_ID` | [SERVICE_CATEGORY_HIST](SERVICE_CATEGORY_HIST.md) | `SVC_CAT_HIST_ID` |

