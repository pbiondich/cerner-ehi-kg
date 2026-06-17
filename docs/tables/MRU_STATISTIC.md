# MRU_STATISTIC

> Usage statistics for choices/decisions made by users allowing those choices to be defaulted the next time a user encounters the same situation

**Description:** Most Recently Used Statistic  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 37

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `MANUAL_DESEL_CNT` | DOUBLE | NOT NULL |  | Number of times this item was manually deselected |
| 6 | `MANUAL_DESEL_RATIO` | DOUBLE |  |  | Manual_desel_cnt/sel_cnt |
| 7 | `MANUAL_SEL_CNT` | DOUBLE | NOT NULL |  | Number of times this item was manually selected |
| 8 | `MANUAL_SEL_RATIO` | DOUBLE |  |  | Manual_sel_cnt/sel_cnt |
| 9 | `MRU_AREA_CD` | DOUBLE | NOT NULL |  | Specifies what mru was invoked |
| 10 | `MRU_CNT` | DOUBLE | NOT NULL |  | Number of times item has recently been selected |
| 11 | `MRU_FACT1_CD` | DOUBLE | NOT NULL |  | Names and meanings of data items used in MRU Selections |
| 12 | `MRU_FACT1_SOURCE` | VARCHAR(30) | NOT NULL |  | Parent_entity_name for the mru fact |
| 13 | `MRU_FACT1_VALUE` | DOUBLE | NOT NULL |  | Parent_entity_id for the mru_fact |
| 14 | `MRU_FACT2_CD` | DOUBLE | NOT NULL |  | Names and meanings of data items used in MRU Selections |
| 15 | `MRU_FACT2_SOURCE` | VARCHAR(30) | NOT NULL |  | Parent_entity_name for the mru fact |
| 16 | `MRU_FACT2_VALUE` | DOUBLE | NOT NULL |  | Parent_entity_id for the mru_fact |
| 17 | `MRU_FACT3_CD` | DOUBLE | NOT NULL |  | Names and meanings of data items used in MRU Selections |
| 18 | `MRU_FACT3_SOURCE` | VARCHAR(30) | NOT NULL |  | Parent_entity_name for the mru fact |
| 19 | `MRU_FACT3_VALUE` | DOUBLE | NOT NULL |  | Parent_entity_id for the mru_fact |
| 20 | `MRU_FACT4_CD` | DOUBLE | NOT NULL |  | Names and meanings of data items used in MRU Selections |
| 21 | `MRU_FACT4_SOURCE` | VARCHAR(30) | NOT NULL |  | Parent_entity_name for the mru fact |
| 22 | `MRU_FACT4_VALUE` | DOUBLE | NOT NULL |  | Parent_entity_id for the mru_fact |
| 23 | `MRU_STATISTIC_ID` | DOUBLE | NOT NULL |  | Primary key |
| 24 | `PRIMARY_FACT_ID` | DOUBLE | NOT NULL |  | Parent_entity_id for the primary fact |
| 25 | `PRIMARY_FACT_MODIFIER` | VARCHAR(50) | NOT NULL |  | Additional specification for the primary fact |
| 26 | `PRIMARY_FACT_SOURCE` | VARCHAR(30) | NOT NULL |  | Parent_entity_name for the primary fact |
| 27 | `PRSNL_COMMUNITY_ID` | DOUBLE | NOT NULL |  | Community this mru is associated to |
| 28 | `PRSNL_COMMUNITY_SOURCE` | VARCHAR(30) | NOT NULL |  | Parent_entity_name for the primary fact |
| 29 | `PRSNL_ID` | DOUBLE | NOT NULL |  | Link to prsnl.person_id |
| 30 | `SELECTION_ID` | DOUBLE | NOT NULL |  | Parent_entity_id of the item to select |
| 31 | `SELECTION_SOURCE` | VARCHAR(30) | NOT NULL |  | Parent_entity_name_of the item to select |
| 32 | `SEL_CNT` | DOUBLE | NOT NULL |  | Number of times item was selected |
| 33 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 34 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 35 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 36 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 37 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

