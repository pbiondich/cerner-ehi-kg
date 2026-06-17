# RC_D_BILL_ITEM

> This table contains bill item information such as activity type and charge description.

**Description:** Revenue Cycle Dimension Bill Item  
**Table type:** REFERENCE  
**Primary key:** `RC_D_BILL_ITEM_ID`  
**Columns:** 26  
**Referenced by:** 5 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVITY_TYPE` | VARCHAR(40) | NOT NULL |  | The type of activity associated with a given bill item. |
| 3 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 4 | `CDM` | VARCHAR(50) |  |  | Charge Description Master Code. A client defined value representing a charge. |
| 5 | `CHARGE_DESCRIPTION` | VARCHAR(200) | NOT NULL |  | The description of a charge associated to a given bill item. |
| 6 | `CPT` | VARCHAR(40) | NOT NULL |  | The Current Procedural Terminology associated to a given bill item. |
| 7 | `CPT_DESCRIPTION` | VARCHAR(200) |  |  | The description of a CPT associated to a given bill item. |
| 8 | `DIAGNOSIS_CODE` | VARCHAR(50) |  |  | Contains diagnosis codes. |
| 9 | `DIAGNOSIS_CODE_DESC` | VARCHAR(200) |  |  | Contains the description of the diagnosis code. |
| 10 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 11 | `FIRST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the first ETL process started that created this record. |
| 12 | `HCPCS` | VARCHAR(200) | NOT NULL |  | Contains the HCFA Common Procedural Coding System associated to a given bill item. |
| 13 | `HCPCS_DESCRIPTION` | VARCHAR(200) |  |  | Contains the description for HCPCS. |
| 14 | `LAST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the last ETL process started that updated this record. |
| 15 | `MILL_BILL_ITEM_ID` | DOUBLE | NOT NULL |  | The bill item identifier from the Millennium Database Bill Item Table. |
| 16 | `MILL_DIAGNOSIS_CD` | DOUBLE | NOT NULL |  | Identifies the code value for the diagnosis code. This column is derived from the code in the Charge_Mod table. |
| 17 | `MILL_LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | Uniquely identifies the logical domain to which the row data belongs. |
| 18 | `PROCEDURE_CODE` | VARCHAR(200) | NOT NULL |  | The procedure code associated to a given bill item. |
| 19 | `PROCEDURE_MODIFIER_TXT` | VARCHAR(3) |  |  | The modifier associated to the Procedure(CPT4 and HCPCS) code. |
| 20 | `RC_D_BILL_ITEM_ID` | DOUBLE | NOT NULL | PK | Uniquely identifies Bill Item information such as activity type and charge description. |
| 21 | `REVENUE_CODE` | VARCHAR(40) | NOT NULL |  | The Revenue Code associated to a given bill item. |
| 22 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 23 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 24 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 25 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 26 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (5)

| From table | Column |
|------------|--------|
| [RC_F_DAILY_CDM_SMRY](RC_F_DAILY_CDM_SMRY.md) | `RC_D_BILL_ITEM_ID` |
| [RC_F_DLY_CHRG_ASSOC_SMRY](RC_F_DLY_CHRG_ASSOC_SMRY.md) | `RC_D_BILL_ITEM_ID` |
| [RC_F_MONTHLY_CDM_SMRY](RC_F_MONTHLY_CDM_SMRY.md) | `RC_D_BILL_ITEM_ID` |
| [RC_F_MTH_CHRG_ASSOC_SMRY](RC_F_MTH_CHRG_ASSOC_SMRY.md) | `RC_D_BILL_ITEM_ID` |
| [RC_F_REVENUE](RC_F_REVENUE.md) | `RC_D_BILL_ITEM_ID` |

