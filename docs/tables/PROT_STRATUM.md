# PROT_STRATUM

> Contains information about stratum associated with an amendment

**Description:** PROT STRATUM  
**Table type:** REFERENCE  
**Primary key:** `PROT_STRATUM_ID`  
**Columns:** 21  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 2 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 3 | `LENGTH_EVALUATION` | DOUBLE |  |  | Indicates the time period during which toxicity will be evaluated |
| 4 | `LENGTH_EVALUATION_UOM_CD` | DOUBLE | NOT NULL |  | Indicates the unit for the evaluation period. It can be Days, Months or Years. |
| 5 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | This field uniquely identifies a row in the organization table. This field identifies the institution responsible for the stratum. For this purpose, an institution can be another hospital, research institute, drug company, government agency, etc. |
| 6 | `PARENT_STRATUM_ID` | DOUBLE | NOT NULL | FK→ | The link back to the stratum_id that this stratum originated or was copied from. |
| 7 | `PROT_AMENDMENT_ID` | DOUBLE | NOT NULL | FK→ | This field uniquely identifies a row in the prot_amendment table. This field identifies the protocol amendment for which this stratum is defined. |
| 8 | `PROT_STRATUM_ID` | DOUBLE | NOT NULL | PK | This is the value of the unique primary identifier of the prot_stratum table. It is an internal system assigned number. |
| 9 | `STATUS_CHG_REASON_CD` | DOUBLE | NOT NULL |  | A code value indicating the reason for change in the status of the stratum. |
| 10 | `STRATUM_CD` | DOUBLE | NOT NULL |  | This field contains a code that identifies the stratum. |
| 11 | `STRATUM_COHORT_TYPE_CD` | DOUBLE | NOT NULL |  | Identifies the type of cohorts. Can be "No Cohort", "Multiple cohort accrue simultaneously" or "One cohort can accrue at a time" |
| 12 | `STRATUM_CTMS_EXTN_TXT` | VARCHAR(255) |  |  | The extension id for the stratum communicated in web service request |
| 13 | `STRATUM_DESCRIPTION` | VARCHAR(2000) |  |  | This field contains a description of the stratum |
| 14 | `STRATUM_ID` | DOUBLE | NOT NULL |  | A logical identifier into the prot_stratum table. No two active rows (rows with end_effective_dt_tm = "31-dec-2100") will have the same stratum_id. |
| 15 | `STRATUM_LABEL` | VARCHAR(100) | NOT NULL |  | A display label for the stratum |
| 16 | `STRATUM_STATUS_CD` | DOUBLE | NOT NULL |  | Status of the stratum. Can be "Open to accrual", or "Closed" or "temporarily suspended" |
| 17 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 21 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `PARENT_STRATUM_ID` | [PROT_STRATUM](PROT_STRATUM.md) | `PROT_STRATUM_ID` |
| `PROT_AMENDMENT_ID` | [PROT_AMENDMENT](PROT_AMENDMENT.md) | `PROT_AMENDMENT_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [PROT_STRATUM](PROT_STRATUM.md) | `PARENT_STRATUM_ID` |

