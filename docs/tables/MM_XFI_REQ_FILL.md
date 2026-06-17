# MM_XFI_REQ_FILL

> Table used to store incoming Requisition Fill interface line transactions. Data is moved from this table to DISTRIBUTION and REQUISITION.

**Description:** MM XFI REQ FILL  
**Table type:** REFERENCE  
**Primary key:** `TRANSACTION_ID`  
**Columns:** 49  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_FLAG` | DOUBLE |  |  | Action flag indicating the action to take place on the transaction. |
| 2 | `AUTO_COMMIT_IND` | DOUBLE |  |  | This field indicates whether to commit the distribution or not. |
| 3 | `BATCH_PROCESSED_DT_TM` | DATETIME |  |  | Stores batch process date time |
| 4 | `BATCH_REF` | VARCHAR(100) |  |  | This is a user defined field; allows a reference number/string to be passed in as part of an interface. |
| 5 | `CONTRIBUTOR` | VARCHAR(40) |  |  | Contributor used to resolve code value alias |
| 6 | `CONTRIBUTOR_CD` | DOUBLE | NOT NULL |  | Contributor used to resolve code value alias |
| 7 | `CREATE_APPLCTX` | DOUBLE |  |  | Application which created this row |
| 8 | `CREATE_DT_TM` | DATETIME |  |  | The date/time this entry was created. |
| 9 | `CREATE_ID` | DOUBLE | NOT NULL |  | ID of user who created this row |
| 10 | `CREATE_TASK` | DOUBLE |  |  | Task which created this row |
| 11 | `EXTENDED_COST` | DOUBLE |  |  | Extended cost of the item quantity. |
| 12 | `FILL_PACK_FACTOR` | DOUBLE |  |  | The filled packaging pack factor. |
| 13 | `FILL_QTY` | DOUBLE |  |  | The filled quantity. |
| 14 | `FILL_UOM` | VARCHAR(20) |  |  | The filled unit of measure. |
| 15 | `FILL_UOM_CD` | DOUBLE | NOT NULL |  | The code value for the fill unit of measure. |
| 16 | `FOREIGN_DIST_NBR` | VARCHAR(20) |  |  | The distribution number from the foreign system. |
| 17 | `FROM_LOCATION` | VARCHAR(60) |  |  | Holds the fill location specified on the requisition. |
| 18 | `FROM_LOCATION_CD` | DOUBLE | NOT NULL |  | Code for the fill location on the requisition. |
| 19 | `ITEM_IDENTIFIER` | VARCHAR(255) |  |  | Identifier used to resolve to an item_id. |
| 20 | `ITEM_IDENTIFIER_TYPE` | VARCHAR(40) |  |  | Type of Identifier being used to resolve an item. |
| 21 | `ITEM_IDENTIFIER_TYPE_CD` | DOUBLE | NOT NULL |  | Code Value of the item identifier type used to resolve an item. |
| 22 | `ITEM_MASTER_ID` | DOUBLE | NOT NULL |  | Foreign key to the item_master table. |
| 23 | `JOB_EXECUTION_ID` | DOUBLE |  | FK→ | Stores the job id when multiple batches of the same scripts are triggered |
| 24 | `LINE_ITEM_ID` | DOUBLE | NOT NULL |  | Foreign key to the line_item table. |
| 25 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 26 | `MISC_CD` | DOUBLE | NOT NULL |  | Miscellaneous Account Codes |
| 27 | `MISC_CODE` | VARCHAR(40) |  |  | Unused at this time. |
| 28 | `ORGANIZATION` | VARCHAR(100) |  |  | The name of the organization on the requisition. |
| 29 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | The identifier of the organization on the requisition. |
| 30 | `PACKAGE_TYPE_ID` | DOUBLE | NOT NULL |  | Foreign key to the package_type table. |
| 31 | `PROCESS_FLAG` | DOUBLE |  |  | Process flag indicating the stage of the interface process. |
| 32 | `PROJECT_CD` | DOUBLE | NOT NULL |  | Project Code Value |
| 33 | `PROJECT_CODE` | VARCHAR(60) |  |  | Unused at this time. |
| 34 | `REQUISITION_ID` | DOUBLE | NOT NULL |  | Foreign key to the requisition table. |
| 35 | `REQ_IDENTIFIER` | VARCHAR(40) |  |  | The requisition number or requisition alias number. Used to resolve to a requisition_id. |
| 36 | `REQ_LINE_NBR` | DOUBLE |  |  | The line number from the requisition. |
| 37 | `SEGMENT_IDENTIFIER` | VARCHAR(10) |  |  | Identifies the type of interface |
| 38 | `SEGMENT_VERSION` | VARCHAR(10) |  |  | The segment version of the upload |
| 39 | `SERIAL_NUMBER` | VARCHAR(40) |  |  | Serial Number. |
| 40 | `TO_LOCATION` | VARCHAR(60) |  |  | The requesting location on the requisition. |
| 41 | `TO_LOCATION_CD` | DOUBLE | NOT NULL |  | The requesting location code on the requisition. |
| 42 | `TRANSACTION_ID` | DOUBLE | NOT NULL | PK | Primary Key |
| 43 | `TRANSFER_FLAG` | DOUBLE | NOT NULL |  | Used to determine whether an average cost is calculated at the fill location. |
| 44 | `UNIT_COST` | DOUBLE |  |  | Unit cost of the item. |
| 45 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 46 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 47 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 48 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 49 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `JOB_EXECUTION_ID` | [JOB_EXECUTION](JOB_EXECUTION.md) | `JOB_EXECUTION_ID` |
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [MM_XFI_REQ_FILL_LOT](MM_XFI_REQ_FILL_LOT.md) | `TRANS_HEADER_ID` |

