# DA_DOMAIN_BV_RELTN

> Contains the relationships between Business domains and Business Views used in Discern Analytics 2.0 metadata.

**Description:** Discern Analytics Domain Business View Relation  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BUS_VIEW_SEQ` | DOUBLE | NOT NULL |  | The sequence value which determines the logical ordering of the view within a domain. |
| 2 | `CORE_IND` | DOUBLE | NOT NULL |  | Indicates this row was created by Cerner. |
| 3 | `DA_BUS_VIEW_ID` | DOUBLE | NOT NULL | FK→ | A business View that is related to this Domain. |
| 4 | `DA_DOMAIN_BV_RELTN_ID` | DOUBLE | NOT NULL |  | Unique, generated number that identifies a single row on the DA_DOMAIN_BV_RELTN table. |
| 5 | `DA_DOMAIN_ID` | DOUBLE | NOT NULL | FK→ | The Domain that is associated with this Business View. |
| 6 | `REQUIRED_IND` | DOUBLE | NOT NULL |  | Indicates whether the business view is required for this domain. Marking a business view in a domain as required forces the SQL engine to include any join statements marked as required in the logical views (contained in the business view) to be included in the SQL along with the tables associated with the join, regardless of what columns have been selected in the query |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DA_BUS_VIEW_ID` | [DA_BUS_VIEW](DA_BUS_VIEW.md) | `DA_BUS_VIEW_ID` |
| `DA_DOMAIN_ID` | [DA_DOMAIN](DA_DOMAIN.md) | `DA_DOMAIN_ID` |

