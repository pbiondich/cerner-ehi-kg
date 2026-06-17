# MM_PRICE_FORMULA

> Formula used to determine the patient price for the supply bill items.

**Description:** Pricing Formula  
**Table type:** REFERENCE  
**Primary key:** `MM_PRICE_FORMULA_ID`  
**Columns:** 12  
**Referenced by:** 4 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `MM_PRICE_FORMULA_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the MM_PRICE_FORMULA table. |
| 3 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | The organization associated with this pricing formula |
| 4 | `PRICE_FORMULA_DESC` | VARCHAR(40) | NOT NULL |  | Text field describing the formula |
| 5 | `PRICE_FORMULA_DESC_KEY` | VARCHAR(40) | NOT NULL |  | This field contains the price_formula_desc value with all special characters removed and all alpha characters converted to upper case. |
| 6 | `PRICE_FORMULA_DESC_KEY_A_NLS` | VARCHAR(160) | NOT NULL |  | Stores the corresponding non-English character set values for the price_formula_desc_key column. Used to sort correctly internationally. |
| 7 | `PRICE_SCHED_ID` | DOUBLE | NOT NULL | FK→ | Price Schedule associated to this pricing formula. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `PRICE_SCHED_ID` | [PRICE_SCHED](PRICE_SCHED.md) | `PRICE_SCHED_ID` |

## Referenced by (4)

| From table | Column |
|------------|--------|
| [MM_CS_PATIENT_PRICE](MM_CS_PATIENT_PRICE.md) | `MM_PRICE_FORMULA_ID` |
| [MM_PRICE_FORMULA_CLASS_R](MM_PRICE_FORMULA_CLASS_R.md) | `MM_PRICE_FORMULA_ID` |
| [MM_PRICE_FORMULA_LOC_RELTN](MM_PRICE_FORMULA_LOC_RELTN.md) | `MM_PRICE_FORMULA_ID` |
| [MM_PRICE_FORMULA_RANGE](MM_PRICE_FORMULA_RANGE.md) | `MM_PRICE_FORMULA_ID` |

