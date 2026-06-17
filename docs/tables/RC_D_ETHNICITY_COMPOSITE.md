# RC_D_ETHNICITY_COMPOSITE

> The Ethnicity Composite Dimension will be a new dimension table that stores the unique list of Ethnicity Combinations.

**Description:** Revenue Cycle Dimension Ethnicity Composite  
**Table type:** REFERENCE  
**Primary key:** `RC_D_ETHNICITY_COMPOSITE_ID`  
**Columns:** 9  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ETHNICITY_COMPOSITE` | VARCHAR(2000) | NOT NULL |  | The Ethnicity Composite is an alphabetical list of each Ethnicity a person identifies as |
| 2 | `FIRST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the first ETL process started that created this record. |
| 3 | `LAST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the last ETL process started that updated this record. |
| 4 | `RC_D_ETHNICITY_COMPOSITE_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the RC_D_ETHNICITY_COMPOSITE table. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (3)

| From table | Column |
|------------|--------|
| [RC_F_DAILY_CENSUS](RC_F_DAILY_CENSUS.md) | `RC_D_ETHNICITY_COMPOSITE_ID` |
| [RC_F_DAILY_CENSUS_SMRY](RC_F_DAILY_CENSUS_SMRY.md) | `RC_D_ETHNICITY_COMPOSITE_ID` |
| [RC_F_MONTHLY_CENSUS_SMRY](RC_F_MONTHLY_CENSUS_SMRY.md) | `RC_D_ETHNICITY_COMPOSITE_ID` |

