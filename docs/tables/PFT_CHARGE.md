# PFT_CHARGE

> Represents the fact that a charge has posted into ProFit Billing system.

**Description:** ProFit Charge  
**Table type:** ACTIVITY  
**Primary key:** `PFT_CHARGE_ID`  
**Columns:** 46  
**Referenced by:** 8 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ACTIVITY_ID` | DOUBLE | NOT NULL | FK→ | FK to the activity_log |
| 6 | `ALT_BILLING_AMT` | DOUBLE | NOT NULL |  | Charge billing amount as calculated using an alternate formula |
| 7 | `ALT_BILLING_QTY` | DOUBLE | NOT NULL |  | Charge quantity as calculated using alternate formula |
| 8 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 9 | `BE_ORG_ID` | DOUBLE | NOT NULL | FK→ | FK to the organization table |
| 10 | `BILLING_AMOUNT` | DOUBLE |  |  | This field reflects the total charge amount minus the credit charges made to this charge. |
| 11 | `BILLING_ENTITY_ID` | DOUBLE | NOT NULL | FK→ | FK to the billing_entity table |
| 12 | `BILLING_QUANTITY` | DOUBLE |  |  | This field reflects the total number of items a charge is for minus the credit charges made to this charge. |
| 13 | `BO_GEN_IND` | DOUBLE |  |  | The indicator that describes if the charge group has generated a claim with the charge on it. |
| 14 | `CHARGE_ITEM_ID` | DOUBLE | NOT NULL | FK→ | FK to the charge table |
| 15 | `CLIENT_BILL_IND` | DOUBLE |  |  | Indicates if the charge will be billed for a client account. |
| 16 | `CLIENT_ORG_ID` | DOUBLE | NOT NULL | FK→ | FK to the organization table |
| 17 | `COLLECTION_PRIORITY_CD` | DOUBLE | NOT NULL |  | Describes the priority of collection. |
| 18 | `CR_ACCT_ID` | DOUBLE | NOT NULL | FK→ | The revenue account associated to the charge. |
| 19 | `CR_ACCT_TEMPL_ID` | DOUBLE | NOT NULL | FK→ | The account template assigned to the revenue account. |
| 20 | `DR_ACCT_ID` | DOUBLE | NOT NULL | FK→ | The A/R account associated to the charge. |
| 21 | `DR_ACCT_TEMPL_ID` | DOUBLE | NOT NULL | FK→ | The account template assigned to the A/R account. |
| 22 | `ENCNTR_TYPE_CD` | DOUBLE | NOT NULL |  | Code value indicating the type of encounter (e.g. Inpatient, outpatient). |
| 23 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 24 | `EXT_BILLED_IND` | DOUBLE | NOT NULL |  | Stores the external_billed_ind value - The value is set to 1 if the charge is billed by the external system, 0 otherwise |
| 25 | `INST_FIN_NBR_KEY` | VARCHAR(250) |  |  | The financial number associated to the charges encounter. |
| 26 | `INTERFACE_ID` | DOUBLE | NOT NULL | FK→ | FK to the csi_log |
| 27 | `LATE_CHRG_FLAG` | DOUBLE |  |  | Describes if the charge was posted after billing has begun. 0 = Not a late charge; 1 = debit late charge; 3 = PBM credit late charge; 4 = adjusted late charge; 5 = manual late charge; 7 = credit late charge; 9 = Regenerate all charges |
| 28 | `MOVE_CHRG_IND` | DOUBLE | NOT NULL |  | ** obsolete ** No longer used. Indicates wheather charge moved from one financial encounter to another. ** obsolete ** |
| 29 | `MV_ORIG_CHRG_ITEM_ID` | DOUBLE |  | FK→ | This Column will be populated with charge item id of the charge which has been moved for the first time.2. Any other workflow on same charge like move charge, financial combine or encntr_mod will copy the same value which has been persisted for first time. |
| 30 | `OFFSET_IND` | DOUBLE |  |  | Describes if the charge has been offset. |
| 31 | `ORIGINAL_UPDT_CNT` | DOUBLE |  |  | Value of the update count on the inserted row. |
| 32 | `PACKAGE_PFT_CHARGE_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the pft_charge related to this package. |
| 33 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Identifies the name of the parent entity. |
| 34 | `PATIENT_LOC_CD` | DOUBLE | NOT NULL |  | Code value identifying the location of the patient. |
| 35 | `PFT_CHARGE_ID` | DOUBLE | NOT NULL | PK | Primary Key |
| 36 | `PFT_CHARGE_STATUS_CD` | DOUBLE | NOT NULL |  | Describes the current status of the charge. |
| 37 | `PFT_CHARGE_STATUS_REASON_CD` | DOUBLE | NOT NULL |  | Describes the status reason for the charge. |
| 38 | `PFT_ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | FK to the pft_encntr table |
| 39 | `PFT_ENCNTR_IND` | DOUBLE |  |  | ProFit Encounter Table |
| 40 | `REPORT_PRIORITY_CD` | DOUBLE | NOT NULL |  | Describes the priority of the report. |
| 41 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL |  | Identifies the Service Resource Code related to this record. |
| 42 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 43 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 44 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 45 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 46 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACTIVITY_ID` | [ACTIVITY_LOG](ACTIVITY_LOG.md) | `ACTIVITY_ID` |
| `BE_ORG_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `BILLING_ENTITY_ID` | [BILLING_ENTITY](BILLING_ENTITY.md) | `BILLING_ENTITY_ID` |
| `CHARGE_ITEM_ID` | [CHARGE](CHARGE.md) | `CHARGE_ITEM_ID` |
| `CLIENT_ORG_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `CR_ACCT_ID` | [ACCOUNT](ACCOUNT.md) | `ACCT_ID` |
| `CR_ACCT_TEMPL_ID` | [ACCT_TEMPLATE](ACCT_TEMPLATE.md) | `ACCT_TEMPL_ID` |
| `DR_ACCT_ID` | [ACCOUNT](ACCOUNT.md) | `ACCT_ID` |
| `DR_ACCT_TEMPL_ID` | [ACCT_TEMPLATE](ACCT_TEMPLATE.md) | `ACCT_TEMPL_ID` |
| `INTERFACE_ID` | [CSI_LOG](CSI_LOG.md) | `INTERFACE_ID` |
| `MV_ORIG_CHRG_ITEM_ID` | [CHARGE](CHARGE.md) | `CHARGE_ITEM_ID` |
| `PACKAGE_PFT_CHARGE_ID` | [PFT_CHARGE](PFT_CHARGE.md) | `PFT_CHARGE_ID` |
| `PFT_ENCNTR_ID` | [PFT_ENCNTR](PFT_ENCNTR.md) | `PFT_ENCNTR_ID` |

## Referenced by (8)

| From table | Column |
|------------|--------|
| [CSI_ERROR_LOG](CSI_ERROR_LOG.md) | `PFT_CHARGE_ID` |
| [PFT_BALANCE](PFT_BALANCE.md) | `PFT_CHARGE_ID` |
| [PFT_BILL_ACTIVITY](PFT_BILL_ACTIVITY.md) | `PFT_CHARGE_ID` |
| [PFT_CHARGE](PFT_CHARGE.md) | `PACKAGE_PFT_CHARGE_ID` |
| [PFT_CHARGE_BO_RELTN](PFT_CHARGE_BO_RELTN.md) | `PFT_CHARGE_ID` |
| [PFT_CHARGE_GLOBAL_DAYS](PFT_CHARGE_GLOBAL_DAYS.md) | `PFT_CHARGE_ID` |
| [PFT_DAILY_BO_HP_CHRG_BAL](PFT_DAILY_BO_HP_CHRG_BAL.md) | `PFT_CHARGE_ID` |
| [PFT_LINE_ITEM_CHRG_RELTN](PFT_LINE_ITEM_CHRG_RELTN.md) | `PFT_CHARGE_ID` |

