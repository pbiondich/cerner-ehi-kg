# DRC_DOSE_RANGE

> This table stores the dose ranges for each type of dose range checks (ie Daily, Single dose, Weekly, Therapy, etc.) These Dose Ranges are related to Premise Groups on the DRC_PREMISE table.

**Description:** DRC Dose Range  
**Table type:** REFERENCE  
**Primary key:** `DRC_DOSE_RANGE_ID`  
**Columns:** 19  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `CUSTOM_IND` | DOUBLE |  |  | Custom Indicator for Dose range. 0 indicates Multum built and 1 indicates Client built. |
| 3 | `DOSE_DAYS` | DOUBLE |  |  | The number of days to use in the checking of N Days Dose. |
| 4 | `DRC_DOSE_RANGE_ID` | DOUBLE | NOT NULL | PK | The unique identifier |
| 5 | `DRC_PREMISE_ID` | DOUBLE | NOT NULL |  | The premise group this range is being built for |
| 6 | `LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | A pointer to text to display to the user if an order was placed with a dose outside of this particular dose. |
| 7 | `MAX_DOSE` | DOUBLE |  |  | For dose range checking, the maximum safe dose for a given medication. |
| 8 | `MAX_DOSE_UNIT_CD` | DOUBLE | NOT NULL |  | The unit of measure for maximum dose. |
| 9 | `MAX_VALUE` | DOUBLE |  |  | The maximum value for the range |
| 10 | `MAX_VARIANCE_PCT` | DOUBLE | NOT NULL |  | Stores a percentage to apply to the MAX VALUE when performing dose range checking |
| 11 | `MIN_VALUE` | DOUBLE |  |  | The minimum value for the range |
| 12 | `MIN_VARIANCE_PCT` | DOUBLE | NOT NULL |  | Stores a percentage to apply to the MIN VALUE when performing dose range checking. |
| 13 | `TYPE_FLAG` | DOUBLE |  |  | The type of dose range |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 19 | `VALUE_UNIT_CD` | DOUBLE | NOT NULL |  | The units of measure for the range |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [DRC_DOSE_RANGE_VER](DRC_DOSE_RANGE_VER.md) | `DRC_DOSE_RANGE_ID` |

