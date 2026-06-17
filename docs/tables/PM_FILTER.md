# PM_FILTER

> This table holds the relationship for a filter.

**Description:** This table contains relationships for a filter and filter values.  
**Table type:** REFERENCE  
**Primary key:** `PM_FILTER_ID`  
**Columns:** 12  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `APP_FLAG` | DOUBLE | NOT NULL |  | Flag used to indicate what type of application the filter is for. |
| 2 | `CODE_SET` | DOUBLE |  |  | Code set used for coded filter type |
| 3 | `FILTER_NAME` | VARCHAR(40) | NOT NULL |  | Name for the filter. |
| 4 | `MULTIPLES_IND` | DOUBLE | NOT NULL |  | Flag that indicates whether filter has multiple default values. |
| 5 | `OPTIONS_BIT` | DOUBLE |  |  | Options bit used to store attributes of the filter |
| 6 | `PM_FILTER_ID` | DOUBLE | NOT NULL | PK | primary key |
| 7 | `TYPE_FLAG` | DOUBLE | NOT NULL |  | Flag used to indicate type for the filter value. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [PM_FILTER_VALUES](PM_FILTER_VALUES.md) | `PM_FILTER_ID` |

