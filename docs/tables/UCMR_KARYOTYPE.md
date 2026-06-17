# UCMR_KARYOTYPE

> This table maintains a list of standard karyotypes.

**Description:** Unified Case Manager Reference - Karyotype  
**Table type:** REFERENCE  
**Primary key:** `UCMR_KARYOTYPE_ID`  
**Columns:** 17  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 4 | `CBO_NOMENCLATURE_ID` | DOUBLE | NOT NULL |  | Uniquely identifies the karyotype in CBO on the nomenclature table that is related to this karyotype. |
| 5 | `COMMON_KARYOTYPE_NAME` | VARCHAR(40) |  |  | This column contains the user defined common name to the karyotype. It is an optional name. |
| 6 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 7 | `KARYOTYPE_TEXT_REF_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the text related to this karyotype. |
| 8 | `PREV_UCMR_KARYOTYPE_ID` | DOUBLE | NOT NULL |  | Used to track versions of the karyotype information. This field will always point back to the initial value created. This may be used to find the correct version when combined with begin and end effective dates and times. |
| 9 | `SHORT_KARYOTYPE_NAME` | VARCHAR(6) |  |  | Contains a short name for the karyotype. Used to indicate that the karyotype is eligible for Frequent. |
| 10 | `UCMR_KARYOTYPE_ID` | DOUBLE | NOT NULL | PK | Uniquely identifies standard karyotypes. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 16 | `VALIDATION_VERSION_TXT` | VARCHAR(10) |  |  | Indicates the version of the validation logic used when validating and associating concepts to this karyotype template. |
| 17 | `VIEW_SEQ` | DOUBLE | NOT NULL |  | This column is used for Frequent karyotypes to indicate an order in which to display them. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `KARYOTYPE_TEXT_REF_ID` | [LONG_TEXT_REFERENCE](LONG_TEXT_REFERENCE.md) | `LONG_TEXT_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [UCMR_KARYOTYPE_CONCEPT](UCMR_KARYOTYPE_CONCEPT.md) | `UCMR_KARYOTYPE_ID` |
| [UCMR_KARYOTYPE_WP_TMPLT_R](UCMR_KARYOTYPE_WP_TMPLT_R.md) | `UCMR_KARYOTYPE_ID` |

