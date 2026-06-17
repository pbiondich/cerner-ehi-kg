# LH_MU_FX_OPS_PARAM

> This table contains Meaningful Use functional reports that should be ran in background

**Description:** LH_MU_FX_OPS_PARAM  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 19

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `AMB_LAB_DENOM` | VARCHAR(20) | NOT NULL |  | Ambulatory Laboratory Denominator Method: 0 = Electronic; 1 = Electronic and Manual |
| 3 | `BR_CCN_ID` | DOUBLE | NOT NULL |  | List of CCN br_ccn_ids |
| 4 | `BR_ELIGIBLE_PROVIDER_ID` | DOUBLE | NOT NULL |  | List of EP's br_eligible_provider_ids |
| 5 | `BR_GPRO_ID` | DOUBLE | NOT NULL |  | Indicates the TIN(s) selected to run through the background report. |
| 6 | `ED_METHOD` | VARCHAR(20) | NOT NULL |  | 1 = All ED Visits; 0 = Overservation Services |
| 7 | `GROUPING_OPTION` | VARCHAR(20) | NOT NULL |  | 1 = Group by CCN/EP; 2 = Group by measure |
| 8 | `LH_MU_FX_OPS_PARAM_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_MU_FX_OPS_PARAM table. |
| 9 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 10 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | List of Organization_ID, for which the MU Report would be executed |
| 11 | `OUTPUT_DEVICE` | VARCHAR(200) |  |  | File to output report |
| 12 | `REPORTING_END_DT_TM` | DATETIME | NOT NULL |  | This column stores the Reporting Period End Date & Time |
| 13 | `REPORTING_START_DT_TM` | DATETIME | NOT NULL |  | This column stores the Reporting Period Start Date & Time |
| 14 | `REPORT_LIST` | VARCHAR(2000) |  |  | List of measures to report |
| 15 | `REPORT_OPTION` | VARCHAR(20) | NOT NULL |  | Report printing type |
| 16 | `REPORT_TYPE` | VARCHAR(20) | NOT NULL |  | Report by: 1 = CCN; 0 = EP |
| 17 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_TASK` | VARCHAR(50) | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |

