# HIM_HAC_CRITERIA

> Stores the criteria combinations of diagnosis codes and procedures codes that qualify for hospital acquired conditions.

**Description:** Health Information Management Hospital Acquired Condition Criteria Table  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `COMPARE_DX_NOMEN_ID` | DOUBLE | NOT NULL | FK→ | The diagnosis nomenclature identifier to compare exists in combination with the nomenclature defined for the criteria. |
| 4 | `COMPARE_DX_PRIMARY_ONLY_IND` | DOUBLE | NOT NULL |  | This indicator determines whether the compare diagnosis nomenclature identifier needs to be primary. |
| 5 | `COMPARE_PX_NOMEN_ID` | DOUBLE | NOT NULL | FK→ | The procedure nomenclature identifier to compare exists in combination with the nomenclature defined for the criteria. |
| 6 | `COMPARE_PX_PRIMARY_ONLY_IND` | DOUBLE | NOT NULL |  | This indicator determines whether the compare procedure nomenclature identifier needs to be primary. |
| 7 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 8 | `HAC_NOMENCLATURE_ID` | DOUBLE | NOT NULL | FK→ | The hospital acquired condition nomenclature identifier to have criteria rules defined. |
| 9 | `HAC_PRIMARY_ONLY_IND` | DOUBLE | NOT NULL |  | This indicator determines whether the hospital acquired condition nomenclature identifier needs to be primary. |
| 10 | `HIM_HAC_CRITERIA_ID` | DOUBLE | NOT NULL |  | This is the unique identifier for the HIM hospital acquired condition code criteria table. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `COMPARE_DX_NOMEN_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |
| `COMPARE_PX_NOMEN_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |
| `HAC_NOMENCLATURE_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |

