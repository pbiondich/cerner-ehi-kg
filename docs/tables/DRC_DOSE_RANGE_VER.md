# DRC_DOSE_RANGE_VER

> History of the DRC_DOSE_RANGE table.

**Description:** DRC Dose range Version  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 19

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `DOSE_DAYS` | DOUBLE |  |  | The number of days to use in the checking of N Days Dose |
| 3 | `DRC_DOSE_RANGE_ID` | DOUBLE | NOT NULL | FK→ | Unique Identifier with ver_seq |
| 4 | `DRC_PREMISE_ID` | DOUBLE | NOT NULL | FK→ | The premise group this range is being built for |
| 5 | `LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | A pointer to text to display to the user if an order was placed with a dose outside of this particular dose. |
| 6 | `MAX_DOSE` | DOUBLE |  |  | For dose range checking, the maximum safe dose for a given medication. |
| 7 | `MAX_DOSE_UNIT_CD` | DOUBLE | NOT NULL |  | The unit of measure for maximum dose. |
| 8 | `MAX_VALUE` | DOUBLE |  |  | The maximum value for the range |
| 9 | `MAX_VARIANCE_PCT` | DOUBLE | NOT NULL |  | Stores a percentage to apply to the MAX_VALUE when performing dose range checking. |
| 10 | `MIN_VALUE` | DOUBLE |  |  | The minimum value for the range |
| 11 | `MIN_VARIANCE_PCT` | DOUBLE | NOT NULL |  | Stores a percentage to apply to the MIN_VALUE when performing dose range checking. |
| 12 | `TYPE_FLAG` | DOUBLE |  |  | The type of dose range |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 18 | `VALUE_UNIT_CD` | DOUBLE | NOT NULL |  | The units of measure for the range |
| 19 | `VER_SEQ` | DOUBLE | NOT NULL |  | version of the drc_dose_range row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DRC_DOSE_RANGE_ID` | [DRC_DOSE_RANGE](DRC_DOSE_RANGE.md) | `DRC_DOSE_RANGE_ID` |
| `DRC_PREMISE_ID` | [DRC_PREMISE](DRC_PREMISE.md) | `DRC_PREMISE_ID` |
| `LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |

