# REQUISITION

> Table used to hold requisition header and template header information

**Description:** Requisition Header/ Template Header  
**Table type:** REFERENCE  
**Primary key:** `REQUISITION_ID`  
**Columns:** 37  
**Referenced by:** 6 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ATTENTION` | VARCHAR(100) |  |  | A string passed as an attention while creating a requisition. |
| 2 | `COMMIT_DT_TM` | DATETIME |  |  | Date/Time when the requisition was committed. |
| 3 | `COMPLETE_DT_TM` | DATETIME |  |  | Date and time the requisition was completed. |
| 4 | `CONFIRMED_BY` | VARCHAR(100) |  |  | *** OBSOLETE *** |
| 5 | `CREATE_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `CREATE_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was inserted. |
| 7 | `CREATE_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the insert of the row in the table. |
| 8 | `CREATE_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that inserted the row. |
| 9 | `DELIVERY_DT_TM` | DATETIME |  |  | Date and time the requisition was created. |
| 10 | `DELIVER_TO_LOCATION_CD` | DOUBLE | NOT NULL |  | *** OBSOLETE *** |
| 11 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 12 | `OMF_SUCCESS_IND` | DOUBLE | NOT NULL |  | The value of 0 or 1 indicates the success or failure of the respective OMF table update. 1 indicates update to OMF table was successful and 0 indicates failure. |
| 13 | `PICK_LIST_PRINT_DT_TM` | DATETIME |  |  | Date/Time when the pick list (report) was printed. |
| 14 | `REFERENCE` | VARCHAR(40) |  |  | *** OBSOLETE *** |
| 15 | `REQUISITION_ID` | DOUBLE | NOT NULL | PK | Unique, generated number that identifies a single row on the REQUISITION table. |
| 16 | `REQ_ALIAS_ID` | DOUBLE | NOT NULL |  | Requisition alias number is used to identify the MMIS matching requisition number with the one in the Procure system. |
| 17 | `REQ_LOCATION_CD` | DOUBLE | NOT NULL |  | The location which is requesting replenishment. |
| 18 | `REQ_NBR` | VARCHAR(40) |  |  | Requisition Number (e.g. 12345-6789) |
| 19 | `REQ_NBR_KEY` | VARCHAR(40) |  |  | Key format field associated to the Requisition Number. |
| 20 | `REQ_NBR_KEY_A_NLS` | VARCHAR(160) |  |  | Stores the corresponding non-English character set values for the req_nbr_Key column. Used to sort correctly internationally. |
| 21 | `REQ_NBR_KEY_NLS` | VARCHAR(82) |  |  | Internationalized Requisition Nbr Key |
| 22 | `REQ_TYPE_CD` | DOUBLE | NOT NULL |  | Holds the code for different requisition types. |
| 23 | `RUSH_IND` | DOUBLE |  |  | This indicator will allow for us to filter on rush requisitions and distributions. |
| 24 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL |  | *** OBSOLETE *** |
| 25 | `SHIP_TO_LOCATION_CD` | DOUBLE | NOT NULL |  | *** OBSOLETE *** |
| 26 | `STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the requisition status. Possible values: Closed, Pendapproval, Committed, Pendcommit, Open, Rejected. |
| 27 | `STATUS_DT_TM` | DATETIME |  |  | The status date and time is used to identify the date and time when the requisition header status is set to "OPEN". |
| 28 | `TEMPLATE_ID` | DOUBLE | NOT NULL |  | *** OBSOLETE *** |
| 29 | `TEMPLATE_NAME` | VARCHAR(100) |  |  | Name of the requisition template. |
| 30 | `TEMPLATE_NAME_KEY` | VARCHAR(100) |  |  | Contains a uppercase equivalent of template name |
| 31 | `TEMPLATE_NAME_KEY_A_NLS` | VARCHAR(400) |  |  | Stores the corresponding non-English character set values for the Template_name_key column. Used to sort correctly internationally. |
| 32 | `TEMPLATE_NAME_KEY_NLS` | VARCHAR(202) |  |  | Contains a uppercase equivalent of template name for internationalization. |
| 33 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 34 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 35 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 36 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 37 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |

## Referenced by (6)

| From table | Column |
|------------|--------|
| [DIST_REQ_R](DIST_REQ_R.md) | `REQUISITION_ID` |
| [LINE_ITEM](LINE_ITEM.md) | `REQUISITION_ID` |
| [MM_APPROVAL_LOG](MM_APPROVAL_LOG.md) | `REQUISITION_ID` |
| [MM_APPROVAL_QUEUE](MM_APPROVAL_QUEUE.md) | `REQUISITION_ID` |
| [MM_APPROVAL_STG](MM_APPROVAL_STG.md) | `REQUISITION_ID` |
| [MM_TRANS_HEADER](MM_TRANS_HEADER.md) | `REQUISITION_ID` |

