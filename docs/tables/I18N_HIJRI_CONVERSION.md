# I18N_HIJRI_CONVERSION

> The i18n_hijri_conversion table will hold the Gregorian and Hijri dates in order to convert between them.

**Description:** i18n hijri conversion  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `GREGORIAN_DT_TM` | DATETIME | NOT NULL |  | Gregorian date corresponding to Hijri_last_day, Hijri_month and Hijri_year. |
| 2 | `HIJRI_LAST_DAY` | DOUBLE |  |  | Hijri last day corresponding to the Gregorian date. |
| 3 | `HIJRI_MONTH` | DOUBLE | NOT NULL |  | Hijri month corresponding to the Gregorian date. |
| 4 | `HIJRI_YEAR` | DOUBLE | NOT NULL |  | Hijri year corresponding to the Gregorian date. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

