# CV_COMPONENT

> Reference table containing components of an algorithm and there atomic tokens.

**Description:** CV COMPONENT  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 24

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ALGORITHM_ID` | DOUBLE | NOT NULL | FK→ | Foreign key for this tableColumn |
| 6 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 7 | `COMPONENT_ID` | DOUBLE | NOT NULL |  | The unique primary key that identifies a row. |
| 8 | `COMPONENT_TYPE_FLAG` | DOUBLE |  |  | 1 : component is used in validating an algorithm 2 : component is used in evaluating an algorithm 0 : component is used in both |
| 9 | `DATA_STATUS_CD` | DOUBLE | NOT NULL |  | Data status indicates a level of authenticity of the row data. Typically this will either be AUTHENTICATED or UNAUTHENTICATED. |
| 10 | `DATA_STATUS_DT_TM` | DATETIME |  |  | The date and time that the data_status_cd was set. |
| 11 | `DATA_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the data_status_cd to be set or change. |
| 12 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 13 | `LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Foreign key. The long_text row contains the textual, postfix notation for the component. |
| 14 | `MNEMONIC` | VARCHAR(50) |  |  | The component name, may be used in other components.Column |
| 15 | `MNEMONIC_KEY` | VARCHAR(50) | NOT NULL |  | The KEY of the mnemonic.Column |
| 16 | `MODIFIER` | DOUBLE |  |  | A value to multiply the result of a component by. A coefficient. If it's set to 0 or 1 it is ignored. |
| 17 | `PARENT_COMPONENT_ID` | DOUBLE | NOT NULL |  | Parent of this component. |
| 18 | `SOURCE_ID` | DOUBLE | NOT NULL |  | Some components consist of tokens that are found in the cv_xref or cv_response table, this is either it's xref_id or response_id, the source_name determines which. |
| 19 | `SOURCE_NAME` | VARCHAR(30) |  |  | Some components consist of tokens that are found in the cv_xref or cv_response table, this is either it's xref_id or response_id, the source_name determines which. |
| 20 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 21 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 22 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 23 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 24 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ALGORITHM_ID` | [CV_ALGORITHM](CV_ALGORITHM.md) | `ALGORITHM_ID` |
| `LONG_TEXT_ID` | [LONG_TEXT_REFERENCE](LONG_TEXT_REFERENCE.md) | `LONG_TEXT_ID` |

