# GL_TRANS_QUALIFIER

> Stores all possible qualifier data as defined at the time a transaction was assigned a GL alias.

**Description:** General Ledger Transaction Qualifier  
**Table type:** ACTIVITY  
**Primary key:** `GL_TRANS_QUALIFIER_ID`  
**Columns:** 48  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCOUNT_SUB_TYPE_CD` | DOUBLE | NOT NULL |  | Contains a sub type of the Acct_Type_Cd to further define the account. |
| 2 | `ACTIVITY_SUB_TYPE_CD` | DOUBLE | NOT NULL |  | Contains a sub type of the activity_type_cd to further define the activity |
| 3 | `ACTIVITY_TYPE_CD` | DOUBLE | NOT NULL |  | A code value that uniquely identifies to which "net" (PathNet, RadNet) and/or what department (General Lab, Microbiology) an order belongs. |
| 4 | `ATTENDING_PHYS_ID` | DOUBLE |  | FK→ | Uniquely identifies the attending physician |
| 5 | `BILLING_ENTITY_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related Billing Entity. |
| 6 | `BILL_ITEM_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related Bill Item. |
| 7 | `BILL_TYPE_CD` | DOUBLE | NOT NULL |  | Identifies the type of bill. |
| 8 | `CLIENT_ACCOUNT_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related account. |
| 9 | `CLIENT_ORG_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related client organization. |
| 10 | `CURRENT_FIN_CLASS_CD` | DOUBLE | NOT NULL |  | The financial classification used for the current balance. |
| 11 | `CURRENT_INS_ORG_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related organization for the current balance. |
| 12 | `DEPARTMENT_CD` | DOUBLE | NOT NULL |  | Service resource code associated to the department. |
| 13 | `ENCNTR_TYPE_CD` | DOUBLE | NOT NULL |  | Categorizes the encounter into a logical group or type. |
| 14 | `ENCNTR_TYPE_CLASS_CD` | DOUBLE | NOT NULL |  | Encounter type class is used to categorize patients into more general groups than encounter type. (i.e., inpatient, outpatient, emergency, recurring outpatient). |
| 15 | `FINANCIAL_CLASS_CD` | DOUBLE | NOT NULL |  | The financial classification used for the encounter. |
| 16 | `GL_TRANS_LOG_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related general ledger transaction log record. |
| 17 | `GL_TRANS_QUALIFIER_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the gl_trans_qualifiers_table. |
| 18 | `HEALTH_PLAN_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related Health Plan. |
| 19 | `INSTITUTION_CD` | DOUBLE | NOT NULL |  | Service resource code associated to the institution. |
| 20 | `INS_ORG_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related insurance organization. |
| 21 | `LEVEL5_CD` | DOUBLE | NOT NULL |  | Service resource code associated to the level 5 (exam room, bench, instrument, etc.) |
| 22 | `LOC_BED_CD` | DOUBLE | NOT NULL | FK→ | The current patient location with a location type of bed |
| 23 | `LOC_BUILDING_CD` | DOUBLE | NOT NULL | FK→ | The current patient location with a location type of building. |
| 24 | `LOC_FACILITY_CD` | DOUBLE | NOT NULL | FK→ | The current patient location with a location type of facility. |
| 25 | `LOC_NURSE_UNIT_CD` | DOUBLE | NOT NULL | FK→ | The current patient location with a location type of nurse unit. |
| 26 | `LOC_ROOM_CD` | DOUBLE | NOT NULL | FK→ | The current patient location with a location type of room |
| 27 | `MED_SERVICE_CD` | DOUBLE | NOT NULL |  | Represents the category of treatment, surgery, or general resources. |
| 28 | `ORDERING_LOCATION_CD` | DOUBLE | NOT NULL |  | Represents the location where the order was placed. |
| 29 | `ORDERING_PHYS_GROUP_ID` | DOUBLE |  | FK→ | Uniquely identifies the ordering physician group. |
| 30 | `ORDERING_PHYS_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the ordering physician. |
| 31 | `PATIENT_LOCATION_CD` | DOUBLE | NOT NULL |  | Identifies the location of the patient. |
| 32 | `PERFORMING_LOCATION_CD` | DOUBLE | NOT NULL |  | Represents the location at which the services were provided. |
| 33 | `PERFORMING_PHYS_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the performing physician. |
| 34 | `PFT_PAYMENT_LOCATION_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related payment location. |
| 35 | `PRIMARY_HEALTH_PLAN_ID` | DOUBLE | NOT NULL | FK→ | The primary health plan ID associated to an activity. |
| 36 | `RENDERING_PHYS_GROUP_ID` | DOUBLE |  | FK→ | Uniquely identifies the rendering physician group. |
| 37 | `SECTION_CD` | DOUBLE | NOT NULL |  | Service resource code associated to the section. |
| 38 | `SUBSECTION_CD` | DOUBLE | NOT NULL |  | Service resource code associated to the subsection. |
| 39 | `SUPERVISING_PHYS_ID` | DOUBLE |  | FK→ | Uniquely identifies the supervising physician. |
| 40 | `TIER_GROUP_CD` | DOUBLE | NOT NULL |  | Tier that was responsible for creating the charge. |
| 41 | `TRANS_REASON_CD` | DOUBLE | NOT NULL |  | Stores information about why a transaction took place. |
| 42 | `TRANS_SUB_TYPE_CD` | DOUBLE | NOT NULL |  | Further identifies the type and purpose of the transaction. |
| 43 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 44 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 45 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 46 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 47 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 48 | `VERIFY_PHYS_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the physician who verified the result. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ATTENDING_PHYS_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `BILLING_ENTITY_ID` | [BILLING_ENTITY](BILLING_ENTITY.md) | `BILLING_ENTITY_ID` |
| `BILL_ITEM_ID` | [BILL_ITEM](BILL_ITEM.md) | `BILL_ITEM_ID` |
| `CLIENT_ACCOUNT_ID` | [ACCOUNT](ACCOUNT.md) | `ACCT_ID` |
| `CLIENT_ORG_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `CURRENT_INS_ORG_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `GL_TRANS_LOG_ID` | [GL_TRANS_LOG](GL_TRANS_LOG.md) | `GL_TRANS_LOG_ID` |
| `HEALTH_PLAN_ID` | [HEALTH_PLAN](HEALTH_PLAN.md) | `HEALTH_PLAN_ID` |
| `INS_ORG_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `LOC_BED_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `LOC_BUILDING_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `LOC_FACILITY_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `LOC_NURSE_UNIT_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `LOC_ROOM_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `ORDERING_PHYS_GROUP_ID` | [PRSNL_GROUP](PRSNL_GROUP.md) | `PRSNL_GROUP_ID` |
| `ORDERING_PHYS_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `PERFORMING_PHYS_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `PFT_PAYMENT_LOCATION_ID` | [PFT_PAYMENT_LOCATION](PFT_PAYMENT_LOCATION.md) | `PFT_PAYMENT_LOCATION_ID` |
| `PRIMARY_HEALTH_PLAN_ID` | [HEALTH_PLAN](HEALTH_PLAN.md) | `HEALTH_PLAN_ID` |
| `RENDERING_PHYS_GROUP_ID` | [PRSNL_GROUP](PRSNL_GROUP.md) | `PRSNL_GROUP_ID` |
| `SUPERVISING_PHYS_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `VERIFY_PHYS_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [GL_TRANS_QUALIFIER_DETAIL](GL_TRANS_QUALIFIER_DETAIL.md) | `GL_TRANS_QUALIFIER_ID` |

