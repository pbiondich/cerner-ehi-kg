# OSM_CLIENT_DEFAULTS

> Stores default values for each cleint to determine process flow in Requisition Order Entry and PathLink..

**Description:** Outreach Services Client Defaults  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 42

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ADMITTING_PHYS_ID` | DOUBLE | NOT NULL | FK→ | The person id of the admitting physician. |
| 2 | `ALIAS_POOL_CD` | DOUBLE | NOT NULL |  | This determines the default alias pool for display in Requisition Order Entry. |
| 3 | `ALIAS_TYPE_CD` | DOUBLE | NOT NULL |  | This determines the default alias for display in Requisition Order Entry. |
| 4 | `BILL_TYPE_FLAG` | DOUBLE |  |  | This determines the default BILL TYPE for display in Requisition Order Entry. |
| 5 | `BILL_TYPE_IND` | DOUBLE |  |  | This determines the default BILL TYPE for display in Requisition Order Entry. [0 = Client, 1= Patient] |
| 6 | `CLIENT_BILL_ENCNTR_TYPE_CD` | DOUBLE | NOT NULL |  | This determines the default ENCNTR TYPE for display in Requisition Order Entry. |
| 7 | `CLIENT_BILL_FIN_CLASS_CD` | DOUBLE | NOT NULL |  | This determines the default financial class for display in Requisition Order Entry. |
| 8 | `CMRN_OPTION_FLAG` | DOUBLE | NOT NULL |  | This setting determines how the Community Medical record Number will be assigned for the patient in Osm's Requisition Order Entry. |
| 9 | `COLLECTION_PRIORITY_CD` | DOUBLE | NOT NULL |  | This determines the default collection priority in Requisition Order Entry. |
| 10 | `COLLECT_BY_PERSON_ID` | DOUBLE | NOT NULL | FK→ | This determines the default COLLECTED PERSON ID for display in Requisition Order Entry. |
| 11 | `COLLECT_BY_USER_IND` | DOUBLE |  |  | This determines if default Collected By is displayed in Requisition Order Entry.[0 - not using current sign on user, 1 - use current sign on user] |
| 12 | `CURDATE_IND` | DOUBLE |  |  | This determines if default CURRENT DATE is displayed in Requisition Order Entry.[0 - no, 1 -yes] |
| 13 | `CURTIME_IND` | DOUBLE |  |  | This determines if default CURRENT TIME is displayed in Requisition Order Entry.[0 - no, 1 -yes] |
| 14 | `ENCOUNTER_TYPE_FLAG` | DOUBLE |  |  | This determines the default ENCOUNTER TYPE for display in Requisition Order Entry. |
| 15 | `FINANCIAL_CLASS_CD` | DOUBLE | NOT NULL |  | This determines the default FINANCIAL CLASS for display in Requisition Order Entry. ************This field is not being used*************************** |
| 16 | `FINANCIAL_CLASS_FLAG` | DOUBLE |  |  | This determines the default FINANCIAL CLASS requirements in Requisition Order Entry. |
| 17 | `FINANCIAL_NUMBER_OPTION_FLAG` | DOUBLE |  |  | This determines financial number assignment in Requisition Order Entry. |
| 18 | `FLEX_REG_FLAG` | DOUBLE |  |  | This determines the flex registration in Requisition Order Entry. |
| 19 | `FLEX_REG_IND` | DOUBLE |  |  | This determines the default use of FLEX REG for Requisition Order Entry. [0 = NO, 1 = YES] *************This field is not being used****************************** |
| 20 | `LOCATION_FLAG` | DOUBLE |  |  | This determines what type of location to show on OSMClientLookup OCX. |
| 21 | `MRN_OPTION_FLAG` | DOUBLE |  |  | This determines how MRN is going to be assigned in Requisition Order Entry. |
| 22 | `NEW_MRN_FLAG` | DOUBLE |  |  | This determines whether to create a new MRN or not in Requisition Order Entry. |
| 23 | `NEW_REG_FLAG` | DOUBLE |  |  | This determines how search returns in Requisition Order Entry. |
| 24 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | Organization id is the key to the table, which identifies the client for which these defaults will be used. |
| 25 | `PATIENT_ALIAS_FLAG` | DOUBLE |  |  | This determines the default action for PATIENT ALIAS in Requisition Order Entry. |
| 26 | `PATIENT_BILL_ENCNTR_TYPE_CD` | DOUBLE | NOT NULL |  | This determines the default PATIENT BILL ENCNTR TYPE for display in Requisition Order Entry. |
| 27 | `PATIENT_BILL_FIN_CLASS_CD` | DOUBLE | NOT NULL |  | This determines the patient bill financial class in Requisition Order Entry. |
| 28 | `PHONE_TYPE_CD` | DOUBLE | NOT NULL |  | This determines the default PHONE TYPE for display in Requisition Order Entry for callback phone numbers. |
| 29 | `PRI_INS_SUB_HP_FLAG` | DOUBLE |  |  | This determines if the primary insurance company, subscriber, and health plan fields are required. |
| 30 | `PRI_SPONSOR_FLAG` | DOUBLE |  |  | This determines if sponsor is required for primary insurance. |
| 31 | `PROCEDURE_VIEW_FLAG` | DOUBLE |  |  | This determines the default View of procedures for display in Requisition Order Entry. |
| 32 | `PROV_HLTH_NBR_FLAG` | DOUBLE | NOT NULL |  | Require provincial health number based on bill type.0 - Required for neither 1 - Required for client bill2 - Required for patient bill3 - Required for both4 - Disabled for both5 - Disabled for client bill6 - Disabled for patient bill |
| 33 | `REV_CYCLE_CONV_DTL_TXT` | VARCHAR(2000) |  |  | Contains the action keys used for the reveneue cycle registration conversation. |
| 34 | `RPT_PRIORITY_CD` | DOUBLE | NOT NULL |  | This determines the default REPORT PRIORITY for display in Requisition Order Entry. |
| 35 | `SEARCH_START_FLAG` | DOUBLE |  |  | This determines the default field used for searching in Requisition Order Entry. |
| 36 | `SUB_MEMBER_NBR_FLAG` | DOUBLE | NOT NULL |  | Require subscriber member number based on bill type. 0 Required for neither 1 Required for client bill 2 Required for patient bill 3 Required for both 4 Disabled for both 5 Disabled for client bill 6 Disabled for patient bill |
| 37 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 38 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 39 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 40 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 41 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 42 | `VETERNARY_IND` | DOUBLE |  |  | This determines the default used to determine if VETERNARY testing is performed for this client for display in Requisition Order Entry. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ADMITTING_PHYS_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `COLLECT_BY_PERSON_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |

