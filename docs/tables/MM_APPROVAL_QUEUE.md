# MM_APPROVAL_QUEUE

> Contains the requisition lines routed for an approval process.

**Description:** Contains the requisition lines set for an approval process.  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 41

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `APPROVAL_AMOUNT` | DOUBLE |  |  | Approval amount. |
| 2 | `APPROVAL_QUEUE_ID` | DOUBLE | NOT NULL |  | Primary key. |
| 3 | `CLASS_NODE_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to class node table. |
| 4 | `COST_CENTER_CD` | DOUBLE | NOT NULL |  | Cost center code value |
| 5 | `CREATE_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `CREATE_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was was inserted. |
| 7 | `CREATE_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the insert of the row in the table. |
| 8 | `CREATE_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted the row. |
| 9 | `CUR_LEVEL` | DOUBLE |  |  | % curent % |
| 10 | `DESCRIPTION` | VARCHAR(40) |  |  | Description of the approval. |
| 11 | `FILL_LOCATION_CD` | DOUBLE | NOT NULL | FK→ | Internal or external location of the item. |
| 12 | `FILL_LOC_COST` | DOUBLE |  |  | Fill location cost. |
| 13 | `IN_PROCESS_IND` | DOUBLE |  |  | Indicator used to determine which lines are currently being processed |
| 14 | `ITEM_DESC` | VARCHAR(255) |  |  | Item description. |
| 15 | `ITEM_ID` | DOUBLE | NOT NULL |  | Foreign key to item master |
| 16 | `ITEM_NBR` | VARCHAR(40) |  |  | Item number. |
| 17 | `LINE_ITEM_ID` | DOUBLE | NOT NULL | FK→ | Foreign Key. |
| 18 | `MIN_APPROVAL_AMOUNT` | DOUBLE |  |  | Minimum approval amount. |
| 19 | `MM_APPROVAL_ID` | DOUBLE | NOT NULL |  | foreign key to mm_approval table. |
| 20 | `MM_APPROVAL_IND` | DOUBLE |  |  | Set to 1 as an approval default. Set to 0 otherwise. Used to recognize a regular approval from a default one. |
| 21 | `NON_CATALOG_IND` | DOUBLE |  |  | Indicator used to determine if the line is a non-catalog item |
| 22 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | The organization that the approval is tied too. Foreign key to organization table. |
| 23 | `ORG_NAME` | VARCHAR(100) |  |  | Organization_Name of the organization tied to the document |
| 24 | `PACKAGE_TYPE_DESC` | VARCHAR(40) |  |  | Package type description. |
| 25 | `PACKAGE_TYPE_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the package type table. It is an internal system assigned number. |
| 26 | `PRICE` | DOUBLE |  |  | %requisito |
| 27 | `PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Foreign key, the prsnl_id of the person from the personnel table (prsnl) |
| 28 | `QTY` | DOUBLE |  |  | %requisito |
| 29 | `REQUISITION_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to requisition |
| 30 | `REQ_AMOUNT` | DOUBLE |  |  | %requisito |
| 31 | `REQ_CREATE_BY` | VARCHAR(40) |  |  | Person who created the requisition. |
| 32 | `REQ_LINE_NBR` | DOUBLE |  |  | Requisition line number. |
| 33 | `REQ_LOCATION_CD` | DOUBLE | NOT NULL |  | Requisition Location Code Value |
| 34 | `REQ_NBR` | VARCHAR(40) |  |  | Requisition number. |
| 35 | `SYSTEM_ITEM_NBR` | VARCHAR(40) |  |  | Internal system assigned number. |
| 36 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 37 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 38 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 39 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 40 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 41 | `VENDOR_CD` | DOUBLE | NOT NULL |  | Internal or external source of the item. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CLASS_NODE_ID` | [CLASS_NODE](CLASS_NODE.md) | `CLASS_NODE_ID` |
| `FILL_LOCATION_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `LINE_ITEM_ID` | [LINE_ITEM](LINE_ITEM.md) | `LINE_ITEM_ID` |
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `REQUISITION_ID` | [REQUISITION](REQUISITION.md) | `REQUISITION_ID` |

