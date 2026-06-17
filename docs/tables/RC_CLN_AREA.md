# RC_CLN_AREA

> This table is used to store temporarily the Fact and Dimension data that has been extracted from the Millennium database and that is going to be loaded in to the data mart tables.

**Description:** Revenue Cycle Clean Area  
**Table type:** ACTIVITY  
**Primary key:** `RC_CLN_AREA_ID`  
**Columns:** 13  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DIMENSION_ID` | DOUBLE | NOT NULL |  | Contains a number that uniquely identifies a dimension table. |
| 2 | `LOAD_STATUS` | VARCHAR(20) | NOT NULL |  | Shows whether the data needs to be loaded (insert or update) or not (i.e. pending or processed status). |
| 3 | `MILL_LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the logical domain to which the row data belongs. |
| 4 | `PARENT_CLN_AREA_ID` | DOUBLE | NOT NULL | FK→ | Identifies the parent ID row in the staging area. |
| 5 | `RCR_GSR_CONTEXT_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related GSR Context Identifier |
| 6 | `RC_CLN_AREA_ID` | DOUBLE | NOT NULL | PK | Contains a number that uniquely identifies a row in the staging area. |
| 7 | `SHR_LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the row on the shared long text table related to this staging area row. |
| 8 | `TABLE_NAME` | VARCHAR(40) | NOT NULL |  | Contains the Name of the Fact or Dimension table to which this data applies. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `MILL_LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |
| `PARENT_CLN_AREA_ID` | [RC_CLN_AREA](RC_CLN_AREA.md) | `RC_CLN_AREA_ID` |
| `RCR_GSR_CONTEXT_ID` | [RCR_GSR_CONTEXT](RCR_GSR_CONTEXT.md) | `RCR_GSR_CONTEXT_ID` |
| `SHR_LONG_TEXT_ID` | [SHR_LONG_TEXT](SHR_LONG_TEXT.md) | `SHR_LONG_TEXT_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [RC_CLN_AREA](RC_CLN_AREA.md) | `PARENT_CLN_AREA_ID` |

