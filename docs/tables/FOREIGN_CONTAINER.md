# FOREIGN_CONTAINER

> Contains description of container information which comes from a foreign system.

**Description:** Foreign Container  
**Table type:** ACTIVITY  
**Primary key:** `FOREIGN_CONTAINER_ID`  
**Columns:** 15  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCESSION_CONTAINER_NBR` | DOUBLE | NOT NULL |  | A number uniquely identifying a particular container on an accession. |
| 2 | `BARCODE_ACCESSION` | VARCHAR(20) | NOT NULL |  | The string printed on a label to uniquely identify the specimen. This string is the accession number truncated. |
| 3 | `CONTAINER_ID` | DOUBLE | NOT NULL | FK→ | The number uniquely identifying the container which utilized this information in its creation in the system. |
| 4 | `CREATED_DT_TM` | DATETIME | NOT NULL |  | The date and time that this foreign container information was created. |
| 5 | `FOREIGN_CONTAINER_ID` | DOUBLE | NOT NULL | PK | Uniquely identifies container information which comes from a foreign system. |
| 6 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related order. |
| 7 | `PARENT_CONTAINER_NBR` | DOUBLE | NOT NULL |  | The number uniquely identifying the parent container on the accession if the container is an aliquot. |
| 8 | `SPEC_CNTNR_CD` | DOUBLE | NOT NULL |  | The specimen container type associated to this container. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 14 | `VOLUME_NBR` | DOUBLE | NOT NULL |  | The total volume of the container. |
| 15 | `VOLUME_UNITS_CD` | DOUBLE | NOT NULL |  | The volume units of measure. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CONTAINER_ID` | [CONTAINER](CONTAINER.md) | `CONTAINER_ID` |
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [FOREIGN_CONTAINER_EXCPTN](FOREIGN_CONTAINER_EXCPTN.md) | `FOREIGN_CONTAINER_ID` |

