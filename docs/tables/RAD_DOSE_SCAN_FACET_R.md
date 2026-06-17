# RAD_DOSE_SCAN_FACET_R

> Stores the facets that are important for this scan.

**Description:** RadNet Dose Scan Facet Relation  
**Table type:** ACTIVITY  
**Primary key:** `RAD_DOSE_SCAN_FACET_R_ID`  
**Columns:** 14  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `LAST_UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time this row was last updated by personnel. |
| 2 | `LAST_UPDT_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | the person that last updated this row. |
| 3 | `RAD_DOSE_FACET_MODALITY_ID` | DOUBLE | NOT NULL | FK→ | Identifies the facet and the modality for this scan. |
| 4 | `RAD_DOSE_SCAN_FACET_R_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the RAD_DOSE_SCAN_FACET_R table. |
| 5 | `RAD_DOSE_SCAN_ID` | DOUBLE | NOT NULL | FK→ | Identifies a scan that is related to this facet and modality. |
| 6 | `UOM_CD` | DOUBLE | NOT NULL |  | *** OBSOLETE **** |
| 7 | `UOM_ID` | DOUBLE | NOT NULL | FK→ | The unit of measure for the facet. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 13 | `VALUE_NBR` | DOUBLE | NOT NULL |  | The numeric value for the facet. |
| 14 | `VALUE_TXT` | VARCHAR(255) |  |  | The string information related to this facet. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LAST_UPDT_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `RAD_DOSE_FACET_MODALITY_ID` | [RAD_DOSE_FACET_MODALITY](RAD_DOSE_FACET_MODALITY.md) | `RAD_DOSE_FACET_MODALITY_ID` |
| `RAD_DOSE_SCAN_ID` | [RAD_DOSE_SCAN](RAD_DOSE_SCAN.md) | `RAD_DOSE_SCAN_ID` |
| `UOM_ID` | [RAD_DOSE_SNOMED_RT_GLOSSARY](RAD_DOSE_SNOMED_RT_GLOSSARY.md) | `RAD_DOSE_SNOMED_RT_GLOSSARY_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [RAD_DOSE_FACET_R_SET](RAD_DOSE_FACET_R_SET.md) | `RAD_DOSE_SCAN_FACET_R_ID` |
| [RAD_DOSE_SCAN_FACET_R_HIST](RAD_DOSE_SCAN_FACET_R_HIST.md) | `RAD_DOSE_SCAN_FACET_R_ID` |

