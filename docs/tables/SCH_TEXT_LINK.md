# SCH_TEXT_LINK

> Scheduling Text Link

**Description:** Scheduling Text Link  
**Table type:** REFERENCE  
**Primary key:** `TEXT_LINK_ID`  
**Columns:** 37  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `CANDIDATE_ID` | DOUBLE | NOT NULL |  | A sequence-generated number to uniquely identify the specific row in the database. |
| 7 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 8 | `EXPERTISE_LEVEL` | DOUBLE | NOT NULL |  | The number of times a user would have to view an object before they are considered an expert. |
| 9 | `LAPSE_UNITS` | DOUBLE | NOT NULL |  | Lapse Units |
| 10 | `LAPSE_UNITS_CD` | DOUBLE | NOT NULL | FK→ | The unique identifier for the lapse units of measure. |
| 11 | `LAPSE_UNITS_MEANING` | VARCHAR(12) |  |  | A 12-character description corresponding to the lapse units of measure. |
| 12 | `MODIFIED_DT_TM` | DATETIME |  |  | The date and time of the last modification. |
| 13 | `NULL_DT_TM` | DATETIME | NOT NULL |  | contains 31-DEC-2100 00:00:00.00. This field is used to maintain foreign keys to tables that contain a VERSION_DT_TM in the primary key. |
| 14 | `PARENT2_ID` | DOUBLE | NOT NULL |  | The unique identifier of the parent object. |
| 15 | `PARENT2_MEANING` | VARCHAR(12) |  |  | A 12-character description corresponding to the PARENT2_ID |
| 16 | `PARENT2_TABLE` | VARCHAR(32) |  |  | The parent table corresponding to the PARENT2_ID |
| 17 | `PARENT3_ID` | DOUBLE | NOT NULL |  | The unique identifier of the parent object. |
| 18 | `PARENT3_MEANING` | VARCHAR(12) |  |  | A 12-character description corresponding to the PARENT3_ID |
| 19 | `PARENT3_TABLE` | VARCHAR(32) |  |  | The parent table corresponding to the PARENT3_ID |
| 20 | `PARENT_ID` | DOUBLE | NOT NULL |  | The unique identifier of the parent object. |
| 21 | `PARENT_MEANING` | VARCHAR(12) |  |  | A 12-character description corresponding to the PARENT_ID |
| 22 | `PARENT_TABLE` | VARCHAR(32) |  |  | The parent table corresponding to the PARENT_ID |
| 23 | `SUB_TEXT_CD` | DOUBLE | NOT NULL | FK→ | The coded identifier for the scheduling sub text type. The sub text types allow for multiple set of text within a text type (prep, post, guidelines, etc.) |
| 24 | `SUB_TEXT_MEANING` | VARCHAR(12) |  |  | The 12-character string corresponding to the scheduling text sub-type. |
| 25 | `TEMPLATE_ACCEPT_CD` | DOUBLE | NOT NULL | FK→ | The coded identifier for the scheduling accept option. |
| 26 | `TEMPLATE_ACCEPT_MEANING` | VARCHAR(12) |  |  | The 12-character string corresponding to the scheduling accept code. |
| 27 | `TEXT_ACCEPT_CD` | DOUBLE | NOT NULL | FK→ | The coded indentifer for the scheduling text accept option. |
| 28 | `TEXT_ACCEPT_MEANING` | VARCHAR(12) |  |  | The 12-character string corresponding to the scheduling accept code. |
| 29 | `TEXT_LINK_ID` | DOUBLE | NOT NULL | PK | The unique identifier for the scheduling text record. |
| 30 | `TEXT_TYPE_CD` | DOUBLE | NOT NULL | FK→ | The coded identifier for the scheduling text type. |
| 31 | `TEXT_TYPE_MEANING` | VARCHAR(12) |  |  | The 12-character string corresponding to the scheduling text type. |
| 32 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 33 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 34 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 35 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 36 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 37 | `VERSION_DT_TM` | DATETIME | NOT NULL |  | The version date and time marks the date the record became historical. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LAPSE_UNITS_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `SUB_TEXT_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `TEMPLATE_ACCEPT_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `TEXT_ACCEPT_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `TEXT_TYPE_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [SCH_USER_LINK](SCH_USER_LINK.md) | `TEXT_LINK_ID` |

