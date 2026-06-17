# CNT_RRF_KEY

> RRF KEY

**Description:** CNT RRF KEY  
**Table type:** REFERENCE  
**Primary key:** `CNT_RRF_KEY_ID`  
**Columns:** 28  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `AGE_FROM_MINUTES` | DOUBLE |  |  | Defines the beginning age in minutes for a defined reference range. |
| 2 | `AGE_FROM_UNITS_CD` | DOUBLE | NOT NULL |  | A unique code value display that identifies the specific age units (such as days, months, years, and so on) for the beginning age reference range. Code Set 340 |
| 3 | `AGE_FROM_UNITS_CDUID` | VARCHAR(100) | NOT NULL |  | Unique identifier FK to CNT_CODE_VALUE_KEY |
| 4 | `AGE_TO_MINUTES` | DOUBLE |  |  | Defines the ending age in minutes for a defined reference range. |
| 5 | `AGE_TO_UNITS_CD` | DOUBLE | NOT NULL |  | A unique code value display that identifies the specific age units (such as days, months, years, and so on) for the ending age reference range. |
| 6 | `AGE_TO_UNITS_CDUID` | VARCHAR(100) | NOT NULL |  | Unique identifier FK to CNT_CODE_VALUE_KEY |
| 7 | `CNT_RRF_KEY_ID` | DOUBLE | NOT NULL | PK | Sequence generated ID |
| 8 | `DCP_REF_RANGE_FACTOR_ID` | DOUBLE | NOT NULL |  | a unique, internal, system-assigned number that identifies a specific reference range factor row. |
| 9 | `ORGANISM_CD` | DOUBLE | NOT NULL |  | Code set: 1021 |
| 10 | `ORGANISM_CDUID` | VARCHAR(100) | NOT NULL |  | Unique identifier FK to CNT_CODE_VALUE_KEY |
| 11 | `PATIENT_CONDITION_CD` | DOUBLE | NOT NULL |  | Code set: 235 |
| 12 | `PATIENT_CONDITION_CDUID` | VARCHAR(100) | NOT NULL |  | Unique identifier FK to CNT_CODE_VALUE_KEY |
| 13 | `PRECEDENCE_SEQUENCE` | DOUBLE | NOT NULL |  | used to determine which reference range row to use when all matching criteria are the same. |
| 14 | `RRF_INTERNAL_UID` | VARCHAR(100) | NOT NULL |  | Unique identifier for domain generated Reference Range factor |
| 15 | `RRF_UID` | VARCHAR(100) | NOT NULL |  | Unique identifier for Reference Range Factor |
| 16 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL |  | A unique code value display that identifies the service resource (such as instrument, bench, or sub section) that will affect the reference range defined. |
| 17 | `SERVICE_RESOURCE_CDUID` | VARCHAR(100) | NOT NULL |  | Unique identifier FK to CNT_CODE_VALUE_KEY |
| 18 | `SEX_CD` | DOUBLE | NOT NULL |  | A unique code value display that identifies the sex adjustment for the reference range. |
| 19 | `SEX_CDUID` | VARCHAR(100) | NOT NULL |  | Unique identifier FK to CNT_CODE_VALUE_KEY |
| 20 | `SPECIES_CD` | DOUBLE | NOT NULL |  | A unique code value display that identifies the species for the defined reference range. |
| 21 | `SPECIES_CDUID` | VARCHAR(100) | NOT NULL |  | Unique identifier FK to CNT_CODE_VALUE_KEY |
| 22 | `SPECIMEN_TYPE_CD` | DOUBLE | NOT NULL |  | A unique code value display that identifies the specimen type for the defined reference range. |
| 23 | `SPECIMEN_TYPE_CDUID` | VARCHAR(100) | NOT NULL |  | Unique identifier FK to CNT_CODE_VALUE_KEY |
| 24 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 25 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 26 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 27 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 28 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (2)

| From table | Column |
|------------|--------|
| [CNT_RRF](CNT_RRF.md) | `CNT_RRF_KEY_ID` |
| [CNT_RRF_AR_R](CNT_RRF_AR_R.md) | `CNT_RRF_KEY_ID` |

