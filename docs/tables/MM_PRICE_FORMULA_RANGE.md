# MM_PRICE_FORMULA_RANGE

> Date ranges for the pricing formula.

**Description:** Pricing Formula Range  
**Table type:** REFERENCE  
**Primary key:** `MM_PRICE_FORMULA_RANGE_ID`  
**Columns:** 31  
**Referenced by:** 4 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `APPLY_FEE_IND` | DOUBLE | NOT NULL |  | Indicator to check whether the fee has to be applied before the markup |
| 3 | `BEGIN_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is considered valid as active current data. |
| 4 | `COST_TYPE_CD` | DOUBLE | NOT NULL |  | The type of costing for this formula. If there is org level tracking, the choices are Org Average or Org Last Cost. If there is location level tracking, the choices are Average and Last Cost. |
| 5 | `DAY_OF_WEEK_FLAG` | DOUBLE | NOT NULL |  | The day of the week that this formula will be updated. |
| 6 | `END_DT_TM` | DATETIME | NOT NULL |  | Date and time on which the pricing formula range ends |
| 7 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 8 | `LAST_UPDT_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The personnel that last updated this row. |
| 9 | `MM_PRICE_FORMULA_ID` | DOUBLE | NOT NULL | FK→ | The pricing formula that this range applies to. |
| 10 | `MM_PRICE_FORMULA_RANGE_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the MM_PRICE_FORMULA_RANGE table. |
| 11 | `MONTHLY_OCCURRENCE_TYPE_FLAG` | DOUBLE | NOT NULL |  | Monthly pattern type selected |
| 12 | `MONTHLY_WEEK_NBR` | DOUBLE | NOT NULL |  | The relative week during a month that recurrence selection is set for. |
| 13 | `NEGATIVE_VARIANCE_AMT` | DOUBLE | NOT NULL |  | Will hold the negative variance percentage or amount. |
| 14 | `NEGATIVE_VARIANCE_TYPE_IND` | DOUBLE | NOT NULL |  | Indicates if the negative variance amount represents a percentage or a monetary amount. |
| 15 | `OCCURRENCE_DAYS` | DOUBLE | NOT NULL |  | The number of days that recurrence selection is set for |
| 16 | `OCCURRENCE_MONTHS` | DOUBLE | NOT NULL |  | The number of months that recurrence selection is set for |
| 17 | `OCCURRENCE_TYPE_FLAG` | DOUBLE | NOT NULL |  | Indicates if the occurrence type is daily, weekly, or monthly. |
| 18 | `OCCURRENCE_WEEKS` | DOUBLE | NOT NULL |  | The number of weeks that recurrence selection is set for |
| 19 | `POSITIVE_VARIANCE_AMT` | DOUBLE | NOT NULL |  | Will hold the positive variance percentage or amount. |
| 20 | `POSITIVE_VARIANCE_TYPE_IND` | DOUBLE | NOT NULL |  | Indicates if the positive variance amount represents a percentage or a monetary amount. |
| 21 | `PREV_MM_PRICE_FORMULA_RANGE_ID` | DOUBLE | NOT NULL | FK→ | The id to the price formula range row before the record was changed. If 0, this is the original unchanged row |
| 22 | `RANGE_DESC` | VARCHAR(40) | NOT NULL |  | Description of pricing formula range |
| 23 | `RANGE_DESC_KEY` | VARCHAR(40) | NOT NULL |  | The value in RANGE_DESC but in all capitals with punctuation removed. This field is used for indexing and searching/ |
| 24 | `RANGE_DESC_KEY_A_NLS` | VARCHAR(160) | NOT NULL |  | Stores the corresponding non-English character set values for the range_desc_key column. Used to sort correctly internationally. |
| 25 | `START_DT_TM` | DATETIME | NOT NULL |  | Date and time on which the pricing formula range begins |
| 26 | `UPDATE_PRICE_FLAG` | DOUBLE | NOT NULL |  | Indicates if the price needs to be updated based on the variance percentage or amount. |
| 27 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 28 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 29 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 30 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 31 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LAST_UPDT_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `MM_PRICE_FORMULA_ID` | [MM_PRICE_FORMULA](MM_PRICE_FORMULA.md) | `MM_PRICE_FORMULA_ID` |
| `PREV_MM_PRICE_FORMULA_RANGE_ID` | [MM_PRICE_FORMULA_RANGE](MM_PRICE_FORMULA_RANGE.md) | `MM_PRICE_FORMULA_RANGE_ID` |

## Referenced by (4)

| From table | Column |
|------------|--------|
| [MM_CS_PATIENT_PRICE](MM_CS_PATIENT_PRICE.md) | `MM_PRICE_FORMULA_RANGE_ID` |
| [MM_PRICE_FORMULA_RANGE](MM_PRICE_FORMULA_RANGE.md) | `PREV_MM_PRICE_FORMULA_RANGE_ID` |
| [MM_RANGE_DETAIL](MM_RANGE_DETAIL.md) | `MM_PRICE_FORMULA_RANGE_ID` |
| [MM_RANGE_PROCESS](MM_RANGE_PROCESS.md) | `MM_PRICE_FORMULA_RANGE_ID` |

