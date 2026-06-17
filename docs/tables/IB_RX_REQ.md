# IB_RX_REQ

> Contains prescription requests from a foreign pharmacy system for an action on an existing prescription (i.e. renewal).

**Description:** Inbound RX Request  
**Table type:** ACTIVITY  
**Primary key:** `IB_RX_REQ_ID`  
**Columns:** 47  
**Referenced by:** 6 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CREATE_DT_TM` | DATETIME |  |  | The time the request was received from the foreign system. |
| 2 | `DAYS_SUPPLY_NBR` | DOUBLE | NOT NULL |  | *** OBSOLETE **** |
| 3 | `DISPENSE_AS_WRITTEN_CD` | DOUBLE | NOT NULL |  | *** OBSOLETE **** |
| 4 | `DISPENSE_QTY` | DOUBLE | NOT NULL |  | The amount of the drug to be dispensed. |
| 5 | `DISPENSE_QTY_UNIT_CD` | DOUBLE | NOT NULL |  | *** OBSOLETE **** |
| 6 | `DRUG_DESCRIPTION_TXT` | VARCHAR(255) |  |  | *** OBSOLETE **** |
| 7 | `GROUP_AVAIL_IND` | DOUBLE | NOT NULL |  | Used to tell whether this prescription request is available to be rolled up with other prescription requests. |
| 8 | `IB_RX_REQ_ID` | DOUBLE | NOT NULL | PK | Unique, generated number that is used to identify an individual row on the IB_RX_REQ table. |
| 9 | `IB_RX_REQ_PERSON_DEMOG_ID` | DOUBLE | NOT NULL | FK→ | Unique number identifying the person demographic this inbound request is for. |
| 10 | `LAST_FILL_DT_TM` | DATETIME |  |  | Deprecated. Date of last fill of prescription from pharmacy. Use with NCPDP Script10.6 or lower specification. |
| 11 | `ORDER_DT_TM` | DATETIME |  |  | Deprecated. Date the prescription was written by the physician. Use with NCPDP Script10.6 or lower specification. |
| 12 | `PHARMACIST_FIRST_NAME` | VARCHAR(255) |  |  | The first name of the pharmacist on the incoming request. |
| 13 | `PHARMACIST_LAST_NAME` | VARCHAR(255) |  |  | The last name of the pharmacist on the incoming request. |
| 14 | `PHARMACIST_MIDDLE_NAME` | VARCHAR(255) |  |  | The middle name of the pharmacist on the incoming request. |
| 15 | `PHARMACIST_PREFIX_NAME` | VARCHAR(255) |  |  | The prefix of the pharmacist's name on the incoming request. |
| 16 | `PHARMACIST_SUFFIX_NAME` | VARCHAR(255) |  |  | The suffix of the pharmacist's name on the incoming request. |
| 17 | `PHARM_CITY_NAME` | VARCHAR(255) |  |  | The name of the pharmacy's city. |
| 18 | `PHARM_COMMENT_TXT` | VARCHAR(255) |  |  | *** OBSOLETE **** |
| 19 | `PHARM_IDENTIFIER` | VARCHAR(255) | NOT NULL |  | The pharmacy that is requesting action on the prescription. |
| 20 | `PHARM_NAME` | VARCHAR(255) |  |  | The name of the pharmacy. |
| 21 | `PHARM_PRIMARY_PHONE` | VARCHAR(80) |  |  | The primary phone number of the pharmacy. |
| 22 | `PHARM_RX_TRANS_IDENT` | VARCHAR(255) |  |  | The unique transaction identifier from the pharmacy system sending the prescription request. |
| 23 | `PHARM_STATE_NAME` | VARCHAR(255) |  |  | The state the pharmacy is located in. |
| 24 | `PHARM_STREET2_ADDR` | VARCHAR(255) |  |  | The second line of the pharmacy's address. |
| 25 | `PHARM_STREET_ADDR` | VARCHAR(255) |  |  | The first line of the pharmacy's address. |
| 26 | `PHARM_ZIP_CODE` | VARCHAR(255) |  |  | The zip code of the pharmacy. |
| 27 | `PRN_IND` | DOUBLE | NOT NULL |  | *** OBSOLETE **** |
| 28 | `PRODUCT_IDENTIFIER` | VARCHAR(255) |  |  | *** OBSOLETE **** |
| 29 | `PROD_IDENT_TYPE_CD` | DOUBLE | NOT NULL |  | *** OBSOLETE **** |
| 30 | `REF_ORDER_ID` | DOUBLE | NOT NULL |  | This is the order identifier referenced on the incoming pharmacy request. This identifier is not guaranteed to match any Millennium order on the domain. |
| 31 | `REMAINING_REFILL_QTY` | DOUBLE | NOT NULL |  | *** OBSOLETE **** |
| 32 | `REQ_TYPE_FLAG` | DOUBLE | NOT NULL |  | Identifies the type of action requested. |
| 33 | `SPECIAL_INSTRUCTIONS_TXT` | VARCHAR(255) |  |  | *** OBSOLETE **** |
| 34 | `SURE_SCRIPT_VERSION_FLAG` | DOUBLE | NOT NULL |  | The version of surescript used to create this inbound request. 0 indicates an undefined version. 1 specifies 8.1, 2 specifies 10.6, 3 specifies NCPDP201701. |
| 35 | `TECH_FIRST_NAME` | VARCHAR(255) |  |  | *** OBSOLETE **** |
| 36 | `TECH_LAST_NAME` | VARCHAR(255) |  |  | *** OBSOLETE **** |
| 37 | `TECH_MIDDLE_NAME` | VARCHAR(255) |  |  | *** OBSOLETE **** |
| 38 | `TECH_PREFIX_NAME` | VARCHAR(255) |  |  | *** OBSOLETE **** |
| 39 | `TECH_SUFFIX_NAME` | VARCHAR(255) |  |  | *** OBSOLETE **** |
| 40 | `TO_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The ID of the intended personnel for the prescription request. |
| 41 | `TRANS_IDENTIFIER` | VARCHAR(255) | NOT NULL |  | The unique transaction identifier from the foreign system sending the prescription request. |
| 42 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 43 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 44 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 45 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 46 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 47 | `ZERO_REFILLS_SPECIFIED_IND` | DOUBLE | NOT NULL |  | *** OBSOLETE **** |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `IB_RX_REQ_PERSON_DEMOG_ID` | [IB_RX_REQ_PERSON_DEMOG](IB_RX_REQ_PERSON_DEMOG.md) | `IB_RX_REQ_PERSON_DEMOG_ID` |
| `TO_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (6)

| From table | Column |
|------------|--------|
| [IB_RX_REQ_ACTION](IB_RX_REQ_ACTION.md) | `IB_RX_REQ_ID` |
| [IB_RX_REQ_DRUG](IB_RX_REQ_DRUG.md) | `IB_RX_REQ_ID` |
| [IB_RX_REQ_FOLLOW_UP](IB_RX_REQ_FOLLOW_UP.md) | `IB_RX_REQ_ID` |
| [IB_RX_REQ_PRSNL_DEMOG](IB_RX_REQ_PRSNL_DEMOG.md) | `IB_RX_REQ_ID` |
| [IB_RX_REQ_SUBTYPE](IB_RX_REQ_SUBTYPE.md) | `IB_RX_REQ_ID` |
| [TASK_SUBACTIVITY](TASK_SUBACTIVITY.md) | `IB_RX_REQ_ID` |

