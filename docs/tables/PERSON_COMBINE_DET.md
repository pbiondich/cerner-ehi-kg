# PERSON_COMBINE_DET

> The person combine detail table contains an audit trail for every row in every table where the person_id was changed to a new person_id as a result of combining two rows in the person table.

**Description:** Person Combine Detail  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 20

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ATTRIBUTE_NAME` | VARCHAR(32) |  |  | Name of the attribute on the child table that is related to person.person_id. |
| 6 | `COMBINE_ACTION_CD` | DOUBLE | NOT NULL |  | The action that was taken on the child row during the combine, e.g. add, update, etc. |
| 7 | `COMBINE_DESC_CD` | DOUBLE | NOT NULL |  | Further describes what happened during a combine. |
| 8 | `ENTITY_ID` | DOUBLE | NOT NULL |  | The value of the primary identifier of the row in the table, identified in the entity_name field, that was combined. For example, if a person_alias row was combined, the value here would be the value of the row's person_alias_id. |
| 9 | `ENTITY_NAME` | VARCHAR(32) | NOT NULL |  | The upper case name of the table to which this row is related (e.g. PRSNL, ORGANIZATION, etc.) |
| 10 | `PERSON_COMBINE_DET_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the person combine detail table. It is an internal system assigned number. |
| 11 | `PERSON_COMBINE_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person combine table. It is an internal system assigned number. |
| 12 | `PREV_ACTIVE_IND` | DOUBLE |  |  | Reference Data Domain Sync (RDDS) use for determining historical occurrences. |
| 13 | `PREV_ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | The value of the active_status_cd prior to the row bein combined. Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 14 | `PREV_END_EFF_DT_TM` | DATETIME |  |  | If a row is made 'not effective' during a combine, the value of its end_effective_dt_tm column before combine is stored here. |
| 15 | `TO_RECORD_IND` | DOUBLE |  |  | If set to 1, this record was originally a child of the to parent record. |
| 16 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 17 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 18 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 19 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 20 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PERSON_COMBINE_ID` | [PERSON_COMBINE](PERSON_COMBINE.md) | `PERSON_COMBINE_ID` |

