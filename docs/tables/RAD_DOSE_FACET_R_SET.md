# RAD_DOSE_FACET_R_SET

> This will contain the Dose facet series details, if the facet has multiple value.

**Description:** RadNet Dose Facet Relation Set  
**Table type:** ACTIVITY  
**Primary key:** `RAD_DOSE_FACET_R_SET_ID`  
**Columns:** 14  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `FACET_VALUE_SEQ` | DOUBLE | NOT NULL |  | The sequence of the values for a facet. |
| 2 | `LAST_UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time this row was last updated by personnel. |
| 3 | `LAST_UPDT_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | the person that last updated this row. |
| 4 | `RAD_DOSE_FACET_R_SET_ID` | DOUBLE | NOT NULL | PK | Unique, generated number that identifies a single row on the RAD_DOSE_FACET_R_SET table. |
| 5 | `RAD_DOSE_SCAN_FACET_R_ID` | DOUBLE | NOT NULL | FK→ | The facet that this value applies to. This is the foreign Key from the table rad_dose_scan_facter_r table |
| 6 | `UOM_CD` | DOUBLE | NOT NULL |  | *** OBSOLETE **** |
| 7 | `UOM_ID` | DOUBLE | NOT NULL | FK→ | The unit of measure the value represents. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 13 | `VALUE_NBR` | DOUBLE | NOT NULL |  | The numeric value for the facet. This can also store code values. |
| 14 | `VALUE_TXT` | VARCHAR(255) |  |  | Stores the string information related to this facet. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LAST_UPDT_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `RAD_DOSE_SCAN_FACET_R_ID` | [RAD_DOSE_SCAN_FACET_R](RAD_DOSE_SCAN_FACET_R.md) | `RAD_DOSE_SCAN_FACET_R_ID` |
| `UOM_ID` | [RAD_DOSE_SNOMED_RT_GLOSSARY](RAD_DOSE_SNOMED_RT_GLOSSARY.md) | `RAD_DOSE_SNOMED_RT_GLOSSARY_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [RAD_DOSE_FACET_R_SET_HIST](RAD_DOSE_FACET_R_SET_HIST.md) | `RAD_DOSE_FACET_R_SET_ID` |

