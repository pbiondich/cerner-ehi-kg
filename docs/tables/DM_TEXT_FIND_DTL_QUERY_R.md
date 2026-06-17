# DM_TEXT_FIND_DTL_QUERY_R

> This table will store the relation between detail rows, and what queries to run against those detail rows.

**Description:** Datbase Management Text Find Detail Query Relation  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `DM_TEXT_FIND_DETAIL_ID` | DOUBLE | NOT NULL | FK→ | Foreign Key back to DM_TEXT_FIND_DETAIL table |
| 3 | `DM_TEXT_FIND_DTL_QUERY_R_ID` | DOUBLE | NOT NULL |  | Primary Key for table |
| 4 | `JOIN_TYPE_FLAG` | DOUBLE | NOT NULL |  | Indicates which join should be used when querying 0 = no join necessary; 1 = AND style join; 2 = Outer join favoring column name hits; 3 = Outer join favoring driver values; 4 = OR style join |
| 5 | `QUERY_GROUP_NAME` | VARCHAR(40) | NOT NULL |  | Indicates which group of queries to row for given DETAIL_ID |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DM_TEXT_FIND_DETAIL_ID` | [DM_TEXT_FIND_DETAIL](DM_TEXT_FIND_DETAIL.md) | `DM_TEXT_FIND_DETAIL_ID` |

