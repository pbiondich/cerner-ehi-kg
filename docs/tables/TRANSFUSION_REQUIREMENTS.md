# TRANSFUSION_REQUIREMENTS

> A reference of valid transfusion requirements that can pertain to patients. This includes antibodies as well as other requirements, such as irradiated blood needed, CMV negative blood needed, etc.

**Description:** Transfusion Requirements  
**Table type:** REFERENCE  
**Primary key:** `REQUIREMENT_CD`  
**Columns:** 15  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ANTI_D_IND` | DOUBLE |  |  | Indicates whether a particular transfusion requirement is the one for Anti-D. This determines how the antigen/antibody validation should work at the time of dispense. If this indicator is set, then the validation will check the Rh type of the product being dispensed, for being negative. |
| 6 | `CHART_NAME` | VARCHAR(40) |  |  | The chart name of the transfusion requirement. (Currently not used). |
| 7 | `CODESET` | DOUBLE |  |  | The number of the codeset from which this transfusion requirement originated, since a transfusion requirement could be an antibody. The two valid code sets for this column are 1611 and 1613. Codeset 1611 is for transfusion requirements that are not antibodies, and codeset 1613 is for antibodies. |
| 8 | `DESCRIPTION` | VARCHAR(50) |  |  | A textual description of the transfusion requirement, as entered by the user in the database tool "AntibodyTool". |
| 9 | `REQUIREMENT_CD` | DOUBLE | NOT NULL | PK | The actual transfusion requirement, whether it be an antibody or other type of transfusion requirement (ex. "CMV Negative", "Irradiation", etc.). This value comes from codeset 1613 if is it an antibody, as indicated by the CODESET column on this table. |
| 10 | `SIGNIFICANCE_IND` | DOUBLE |  |  | Indicates whether this antibody is clinically significant or not, used during an electronic crossmatch. A value of 1 indicates clinical significance. A value of 0 indicates no clinical significance. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [TRANS_REQ_R](TRANS_REQ_R.md) | `REQUIREMENT_CD` |

