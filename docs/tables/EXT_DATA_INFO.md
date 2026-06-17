# EXT_DATA_INFO

> This table stores infromation about external data including status and links to the source document and chart data.

**Description:** external data information  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 24

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_DT_TM` | DATETIME |  |  | The date and time of the action |
| 2 | `ACTION_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The personnel who performed the action |
| 3 | `CHART_REFERENCE_ID` | DOUBLE | NOT NULL |  | The id on the table of the charted data |
| 4 | `CHART_REFERENCE_NAME` | VARCHAR(30) |  |  | The table name of the charted data related to the external data. |
| 5 | `DATA_SOURCE_CD` | DOUBLE | NOT NULL |  | The source of the external data. |
| 6 | `DATA_SOURCE_NAME` | VARCHAR(100) |  |  | The name of the source for the external data |
| 7 | `DATA_STATUS_CD` | DOUBLE | NOT NULL |  | Data status indicates a level of authenticity of the row data. Typically this will either be AUTHENTICATED or UNAUTHENTICATED. |
| 8 | `DATA_TYPE_CD` | DOUBLE | NOT NULL |  | Type of the external data. ALLERGIES, IMMUNIZATION |
| 9 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | The Encounter related to the External Data |
| 10 | `EXT_DATA_CLOB_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for the external clob data. |
| 11 | `EXT_DATA_GROUP_ID` | DOUBLE |  | FK→ | The unique identifier for the external grouped data. |
| 12 | `EXT_DATA_INFO_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 13 | `LONG_TEXT_ID` | DOUBLE | NOT NULL |  | Identifier of the external data if stored in the long_text table. |
| 14 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | The person related to the external data. |
| 15 | `REQUESTED_ACTION_CD` | DOUBLE | NOT NULL |  | Action requested for the data. Values include ADD, UPDATE, REMOVE |
| 16 | `REQUESTED_ACTION_DT_TM` | DATETIME |  |  | The date and time of the requested action. |
| 17 | `REQUESTED_ACTION_DT_TM_FLAG` | DOUBLE |  |  | Indicates precision of the requested_action_dt_tm.0 = date/time; 1 = date/time to second; 2 = date/time to minute; 3 = date/time to hour; 4 = date to day; 5 = date to month; 6 = date to year |
| 18 | `SOURCE_REFERENCE_ID` | DOUBLE | NOT NULL |  | The id on the table of the source of the external data. |
| 19 | `SOURCE_REFERENCE_NAME` | VARCHAR(30) |  |  | The table name of the source of the external data. |
| 20 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 21 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 22 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 23 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 24 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACTION_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `EXT_DATA_CLOB_ID` | [EXT_DATA_CLOB](EXT_DATA_CLOB.md) | `EXT_DATA_CLOB_ID` |
| `EXT_DATA_GROUP_ID` | [EXT_DATA_GROUP](EXT_DATA_GROUP.md) | `EXT_DATA_GROUP_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

