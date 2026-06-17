# INTERFACE_FILE

> Contains information about how charges will be written to the inteface_charge table.

**Description:** Interface File  
**Table type:** REFERENCE  
**Primary key:** `INTERFACE_FILE_ID`  
**Columns:** 37  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 3 | `BATCH_FREQUENCY` | DOUBLE |  |  | not used. |
| 4 | `BILLING_ENTITY_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the Billing Entity related to this interface file. |
| 5 | `CDM_ID_SUSPEND_IND` | DOUBLE |  |  | Indicates whether the charges for this interface file will suspend if not linked to a CHARGE_DESC_MASTER_ID. |
| 6 | `CDM_SCHED_CD` | DOUBLE | NOT NULL |  | Indicates which cdm schedule of bill code to look for before posting the charge to the interface_charge table. If the cdm from that particular schedule is not there, it will be marked as suspended. If the code value with a cdf_meaning of "ALL" is in this field, then if there isn't a cdm at all on the charge, it will suspend. If this is 0, the charge can successfully be written to the interface_charge table without a bill code in this schedule. |
| 7 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 8 | `COST_CENTER_SUSPEND_IND` | DOUBLE |  |  | Indicates whether the charges for this interface file will suspend if not linked to a cost center. |
| 9 | `CPT_SCHED_CD` | DOUBLE | NOT NULL |  | Indicates which cpt schedule of bill code to look for before posting the charge to the interface_charge table. If the cpt from that particular schedule is missing, the charge will be marked as suspended. If the code value with the cdf_meaning of "ALL" is in this field, then if the charge is missing a cpt at all, the charge will suspendd. If this is 0, the charge can successfully be written to the interface_charge table without a bill code in this schedule. |
| 10 | `DESCRIPTION` | VARCHAR(100) | NOT NULL |  | A description of the interface file, such as "T01". Do not use spaces or periods in this name. |
| 11 | `DOC_NBR_CD` | DOUBLE | NOT NULL |  | Value that indicates whether the doctor numbers written to the interface_charge table will be UPIN or organization identifiers. It defaults to the organization identifier. |
| 12 | `EXPLODE_IND` | DOUBLE |  |  | Indicates what afc_post_interface_charge will do with the quantity column. If this indicator is 1, the quantity will not be written to the interface_charge table, but will instead "explode" into that number of interface_charge records with a quantity of 1. If the indicator is 0, the quantity will be written to the interface_charge table. |
| 13 | `FILE_NAME` | VARCHAR(32) |  |  | The name of the file to be created by the interface program, including the directory in which to put the file, such as "CER_SCRIPT:T01.DAT". This file name cannot be longer than 30 characters (including the path name). |
| 14 | `FIN_NBR_SUSPEND_IND` | DOUBLE |  |  | If this value is a 1, then if a charge is missing a financial number, it will be marked as suspended by afc_post_interface_charge. If the value is a 0, then if the charge is missing a financial number, it will not be marked as suspended and will be processed like any other pending charge. |
| 15 | `HL7_IND` | DOUBLE |  |  | Indicates whether or not an interface file is HL7 instead of batch proprietary. |
| 16 | `HOLD_PERIOD` | DOUBLE |  |  | not used. |
| 17 | `INTERFACE_FILE_ID` | DOUBLE | NOT NULL | PK | This is the value of the unique primary identifier of the interface_file table. It is an internal system assigned number. |
| 18 | `INTERFACE_TYPE_FLAG` | DOUBLE | NOT NULL |  | Defines an interface file type for use in other Millennium solutions. |
| 19 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 20 | `MAX_FT1` | CHAR(5) |  |  | If the hl7_ind is checked for the interface_file, the number in this column is maximum number of FT1's that can be sent per detail segment. This number is pulled from code set 23169. The default is 15, so if this column has a value of 0 in it, 15 will be the maximum number of FT1's. |
| 21 | `MULT_BILL_CODE_SCHED_CD` | DOUBLE | NOT NULL |  | This determines from what bill code schedule the extra bill codes on the interface_charge table will come. This affects bill_code1, bill_code2, bill_code3, bill_code1_desc, bill_code2_desc, bill_code3_desc. |
| 22 | `ORDER_PHYS_COPY_IND` | DOUBLE | NOT NULL |  | This column holds a value of 1 if the ord_phys_id on the charge table will be copied to the verify_phys_id of the charge table when verify_phys_id is empty. |
| 23 | `PERF_PHYS_CONT_IND` | DOUBLE |  |  | This field holds a value of 0 if the perf_phys_id on the interface_charge table will be populated with the verify_phys_id from the charge table or a 1 if the perf_phys_id on the interface_charge table will be populated with the perf_phys_id from the charge table. |
| 24 | `PROFIT_TYPE_CD` | DOUBLE | NOT NULL |  | This code value is the billing indicator for a particular interface file. It specifies what type of billing is done, whether it be patient accounting or client billing, in each interface file. |
| 25 | `REALTIME_IND` | DOUBLE |  |  | Indicates whether the charges for this interface file are transmitted realtime. The alternative to realtime is batch. |
| 26 | `REPROCESS_CPT_IND` | DOUBLE | NOT NULL |  | Determines whether or not charges that have this interface file should be reprocessed due to an encounter modification. 0 - Don't reprocess changes when an encounter modification occurs and the CPT code changes; 1- Reprocess changes when an encounter modification occurs and the CPT code changes. |
| 27 | `REPROCESS_IND` | DOUBLE | NOT NULL |  | Determines whether or not charges that have this interface file should be reprocessed due to an encounter modification. 0 - Don't reprocess changes when an encounter modification occurs; 1 - reprocess changes when an encounter modification occurs. |
| 28 | `REV_SCHED_CD` | DOUBLE | NOT NULL |  | Stores the revenue code schedule. Used to determine if a charge should be suspended or not if they are missing the specified revenue code schedule. |
| 29 | `ROUND_METHOD_FLAG` | DOUBLE |  |  | Standard Rounding = 0, Always Round Up = 1, Always Round Down = 2. Defines how rounding should occur for non-Profit JCode processing |
| 30 | `SERVICE_BASED_IND` | DOUBLE |  |  | Indicates whether or not an interface tile is service based. |
| 31 | `SF_HL7_IND` | DOUBLE |  |  | Indicates that this interface file is used for Sorian Financials HL Interface. |
| 32 | `SUSP_CHRG_PROCESS_FLAG` | DOUBLE | NOT NULL |  | Defines how the suspended charges should be dealt with during the encounter mods process.0 - Disable 1 - Enable |
| 33 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 34 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 35 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 36 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 37 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BILLING_ENTITY_ID` | [BILLING_ENTITY](BILLING_ENTITY.md) | `BILLING_ENTITY_ID` |
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [BT_COND_CRIT_GRP_RELTN](BT_COND_CRIT_GRP_RELTN.md) | `INTERFACE_FILE_ID` |
| [CHARGE](CHARGE.md) | `INTERFACE_FILE_ID` |

