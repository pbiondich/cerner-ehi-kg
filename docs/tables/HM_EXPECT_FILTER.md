# HM_EXPECT_FILTER

> Health Maintenance Expectation Filter

**Description:** HM_EXPECT_FILTER  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `EXPECT_ID` | DOUBLE | NOT NULL | FK→ | The identifier of the Expectation to which this filter is associated. FK value from HM_EXPECT table. |
| 2 | `FILTER_ENTITY_ID` | DOUBLE | NOT NULL |  | The identifier of the Filter Entity. This will be the Primary Key on the table identified in the FILTER_ENTITY_NAME. |
| 3 | `FILTER_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | The Name of the Filter Entity. This will normally be the table from which the filter originated. |
| 4 | `HM_EXPECT_FILTER_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `EXPECT_ID` | [HM_EXPECT](HM_EXPECT.md) | `EXPECT_ID` |

